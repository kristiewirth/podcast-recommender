## Find Your New Favorite Podcast!

<img src='images/mic-image.jpg' width='400'>

### Introduction

This project aims to provide recommendations for new podcasts based on the podcasts you already know and love. Using methods such as natural language processing, cosine similarities, and Flask, this interactive tool will be useful for anyone wishing to expand their current podcast library.

This project is currently in progress, so stay tuned for more updates!

### Data

* [Podcast dataset](https://github.com/ageitgey/all-podcasts-dataset)

### Methods

The first step in this project was to process the podcast description text into a machine-readable form using Natural Language Processing.

Steps taken in the cleaning process included:
* Changing all text to lowercase
* Lemmatizing the text (i.e., reducing a word to its stem and utilizing contextual information)
* Removing stop words from the text (i.e., commonly used words such as 'the' and 'a')

### Repository Layout

    ├── README.md               <- The top-level README with a project summary
    │
    ├── data/                   <- All data sets used for this project
    │
    ├── models/                 <- Trained and serialized models, model predictions, or model summaries
    │
    ├── images/                 <- All images used through this project
    │
    ├── src/                    <- Source code for use in this project
    │   ├── __init__.py         <- Makes the src folder into a Python module
    │   ├── run.py              <- Script that runs the entire project pipeline in order
    │   └── EDA.ipynb           <- Notebook for exploratory data analysis
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment;
    │                              generated with `pipreqs .`;
    │                              can be installed using `pip install -r requirements.txt`
    │
    ├── references/             <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── web_app/                <- Files for the project's web application
    │   ├── app.py              <- Main file to run web app
    │   ├── templates/          <- HTML files
    │   └── static/             <- Files for modifying web app design
    │       ├── css/            <- CSS files
    │       ├── fonts/          <- Font customizing files
    │       └── js/             <- Javascript files
    │
    ├── deliverables/           <- Final output for the project - presentation slides, written analysis, etc.

### Results and Applications

Coming soon.

|Measure|Final Test Score|
| :-------------: |:-------------:|
|_|_|

### Tech Stack

* Python
* Pandas
* Spacy

### References and Acknowledgements

* Repository layout inspired by the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/).
