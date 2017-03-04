from collections import Counter
import string
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
from bag_of_words import Bag_of_words
import numpy as np 

class Extract_Features():

	def __init__(self, x):
		self.data_reviews = x
		self.len_and_char_count = None
		self.word_unique_count = None
		self.sentence_count = None
		self.ari_index = None
		self.stars = None
		self.outcomes = None
		self.feature_concat = None

	def get_features_concat(self):
		self.len_and_char_count = []
		self.word_unique_count = []
		self.sentence_count = []
		self.ari_index = []
		self.stars = []
		self.feature_concat = np.array([])

		i = 0 
		tokenizer = RegexpTokenizer(r'\w+')

		for r in tqdm(self.data_reviews):

			self.len_and_char_count.append(self.get_textlength(r))
			self.word_unique_count.append(self.word_counter(tokenizer, r))
			self.sentence_count.append(self.sentence_counter(r))
			self.ari_index.append(self.ari_score(i))
			self.stars.append(self.review_stars(r))
			i+=1

		self.len_and_char_count = np.array(self.len_and_char_count)
		self.word_unique_count = np.array(self.word_unique_count)
		self.sentence_count = np.array(self.sentence_count)
		self.ari_index = np.array(self.ari_index)
		self.stars = np.array(self.stars)

		self.feature_concat = np.concatenate((self.len_and_char_count, \
											self.word_unique_count, \
											self.sentence_count, \
											self.ari_index, \
											self.stars), axis=1)
		return self.feature_concat


	def get_textlength(self, r):
		temp = [len(r["reviewText"]), self.count_letters(r["reviewText"])]
		return temp

	def count_letters(self, review, valid_letters=string.ascii_letters):
		count = Counter(review)
		return sum(count[letter] for letter in valid_letters)

	def word_counter(self, tokenizer, r):
		tokens = tokenizer.tokenize(r["reviewText"])
		return [len(tokens), len(set(tokens))]


	def sentence_counter(self, r):
		return [len(sent_tokenize(r["reviewText"]))]

	def ari_score(self, x):
		return [4.71*(self.len_and_char_count[x][1]/self.word_unique_count[x][1])+0.5*(self.word_unique_count[x][1]/self.sentence_count[x][0])]

	def review_stars(self, r):
		return [int(r["overall"])]

	def outcome_variable(self):
		self.outcomes = [r["helpful"][0]/(1.0*r["helpful"][1]) for r in self.data_reviews]
		return self.outcomes

	def bag_of_words(self):
		bow = Bag_of_words(self.data_reviews)
		clean_train_reviews = bow.gen_bag_for_all()
		features = bow.train_bag(clean_train_reviews)
		return features

		