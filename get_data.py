import gzip
from tqdm import tqdm

class Get_Data():

	def __init__(self):
		self.data = None

	def parse(self, path):
		self.data = []
		g = open(path, 'r')
		for l in tqdm(g):
			l = eval(l)
			l["reviewText"] = l["summary"]+l["reviewText"]
			self.data.append(l)
		return self.data

	def split_into_train_test(self, ratio):
		pass