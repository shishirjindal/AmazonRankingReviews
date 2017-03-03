from collections import Counter
import string
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from tqdm import tqdm

class Extract_Features():

	def __init__(self, x):
		self.data_reviews = x
		self.len_and_char_count = None
		self.word_unique_count = None
		self.sentence_count = None
		self.ari_index = None
		self.review_stars = None

	def get_textlength(self):
		self.len_and_char_count = {}
		i = 0
		for r in tqdm(self.data_reviews):
			self.len_and_char_count[i] = [len(r["reviewText"]), self.count_letters(r["reviewText"])]
			i += 1
		return self.len_and_char_count

	def count_letters(self, review, valid_letters=string.ascii_letters):
		count = Counter(review)
		return sum(count[letter] for letter in valid_letters)

	def word_counter(self):
		self.word_unique_count = {}
		i = 0
		tokenizer = RegexpTokenizer(r'\w+')
		for r in tqdm(self.data_reviews):
			tokens = tokenizer.tokenize(r["reviewText"])
			self.word_unique_count[i] = [len(tokens), len(set(tokens))]
			i += 1
		return self.word_unique_count


	def sentence_counter(self):
		i = 0
		self.sentence_count = []
		for r in tqdm(self.data_reviews):
			self.sentence_count.append(len(sent_tokenize(r["reviewText"])))
			if self.sentence_count[i]==0:
				print r
			i += 1
		return self.sentence_count

	def ari_score(self):
		self.ari_index = [4.71*(self.len_and_char_count[x][1]/self.word_unique_count[x][1])+0.5*(self.word_unique_count[x][1]/self.sentence_count[x]) \
						for x in range(len(self.sentence_count))]

	def review_stars(self):
		self.review_stars = [int(r["overall"]) for r in self.data_reviews]

	def bag_of_words(self):
		pass
		