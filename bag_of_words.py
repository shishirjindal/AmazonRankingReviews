import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import get_data
import re

class Bag_of_words():

    def __init__(self, data):
        self.data_reviews = data

    def gen_bag_for_all(self):
        clean_train_reviews = []
        for r in self.data_reviews:
            clean_train_reviews.append(" ".join(self.review_to_wordlist(r["reviewText"], True)))
        return clean_train_reviews


    def train_bag(self, clean_train_reviews):
        self.vectorizer = CountVectorizer(analyzer = "word",   \
                                 tokenizer = None,    \
                                 preprocessor = None, \
                                 stop_words = None,   \
                                 max_features = 5000)

        self.train_data_features = self.vectorizer.fit_transform(clean_train_reviews)
        self.train_data_features = train_data_features.toarray()
        return self.train_data_features


    def review_to_wordlist(self, review, remove_stopwords=False ):
        review_text = re.sub("[^a-zA-Z\-']"," ", review)
        words = review_text.lower().split()
        if remove_stopwords:
            stops = set(stopwords.words("english"))
            words = [w for w in words if not w in stops]
        return (words)
