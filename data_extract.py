import gzip
from tqdm import tqdm

def filterByVote(l):
	if (l['helpful'][1])>10:
		return True
	return False

superdict = {}

def IdStore(l):
	if l['asin'] not in superdict:
		superdict[l['asin']] = 1 
	else :
		superdict[l['asin']] += 1

f = open('filtered_reviews','w')

def parse(path):
	g = gzip.open(path, 'r')
	for l in tqdm(g):
		l = eval(l)
		IdStore(l)
	g = gzip.open(path, 'r')
	for l in tqdm(g):
		l =  eval(l)
		if(filterByVote(l) and (superdict[l['asin']]>15)):
			f.write(str(l)+'\n')

parse("./reviews_Toys_and_Games.json.gz")
f.close()