from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import spacy
import re
import string
import os
import pandas as pd
import numpy as np


def lematize(docs):
    # Remove punctuation
    punc_list = set(string.punctuation)
    no_punc = ''.join([char for char in docs if char not in punc_list])

    # Remove unicode
    printable = set(string.printable)
    no_uni = ''.join([char for char in no_punc if char in printable])

    # Run the doc through spaCy
    nlp = spacy.load('en')
    spacy_doc = nlp(no_uni)

    # Lemmatize and lower text
    # re.sub is finding any non-alphanumeric chars and substituting with empty string
    tokens = [re.sub('\W+', '', token.lemma_.lower()) for token in spacy_doc]
    return tokens


if __name__ == '__main__':
    # Setting empty dataframe
    df = pd.DataFrame()

    # Iterating through all tsv files
    path = '../data/'
    for filename in os.listdir(path):
        # Loading each tsv file as dataframe
        temp_df = pd.read_csv(path + filename, sep='\t', header=None)
        # Concating new tsv file to current df
        df = pd.concat([df, temp_df], axis=0)

    # Setting column names
    df.columns = ['permalink', 'name', 'image_url', 'feed_url', 'website_url', 'itunes_owner_name',
                  'itunes_owner_email', 'managing_editor_name', 'managing_editor_email', 'explicit',
                  'description', 'itunes_summary']

    # Limiting df to just podcast name & description for now - may add in other features later
    df = df[['name', 'description']]

    # Sorting by description
    df.sort_values('description', inplace=True)

    # Dropping duplicates by description (some podcasts are listed multiple times by platform)
    df.drop_duplicates('description', inplace=True)
    df.reset_index(inplace=True, drop=True)

    # Taking a small sample for testing - will remove later
    df = df.head()

    # Adding domain specific stop words - will create a histogram to determine any
    # other frequently occuring words that don't add meaning here
    stop_words = set(list(ENGLISH_STOP_WORDS) +
                     ['podcast', 'show', 'mp3', 'android', 'iphone', 'ipad'])

    # Instantiating tfidf vectorizer
    vectorizer = TfidfVectorizer(stop_words=stop_words, tokenizer=lematize)

    # Getting vectors from podcast descriptions
    vectors = vectorizer.fit_transform(df['description'])
    # Changing vectors to a pandas dataframe
    vectors = pd.DataFrame(vectors.todense())
    # Setting the tokens as the column names
    words = vectorizer.get_feature_names()
    vectors.columns = words
    df = pd.concat([df, vectors], axis=1)

    # Compare the documents to themselves; higher numbers are more similar
    # The diagonal is comparing a document to itself, so those are 1's (100% similar)
    cos_sims = linear_kernel(vectors, vectors)
    # Removing 1's on the diagonals
    np.place(cos_sims, cos_sims >= 0.99, 0)

    # Getting the podcast that is most similar for each podcast
    # most_similar = cos_sims.argmax(axis=0)
    most_similar = cos_sims.argsort(axis=1)[::-1]
    df['most_similar'] = list(df['name'][most_similar])
