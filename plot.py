import gzip
import math
import matplotlib.pyplot as plt
from tqdm import tqdm


def parse(x):
	new_x = []
	for k in tqdm(x):
		new_x.append(k["helpful"][0]/(1.0*k["helpful"][1]))
	print len(new_x)
	return new_x


def show_histogram(x, xlabel, ylabel, title):
	plt.hist(x, bins = 30)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.title(title)
	plt.show()

def render(x):
	x = parse(x)
	ylabel = "Count"
	xlabel = 'upvotes/total votes'
	title = 'Histogram of helpfulness'
	show_histogram(x, xlabel, ylabel, title)