import features
import get_data
import plot
from bag_of_words import Bag_of_words
import numpy as np

if __name__ == '__main__':

	data_getter = get_data.Get_Data()
	data_reviews = data_getter.parse("./filtered_reviews")


	feature_extracter = features.Extract_Features(data_reviews)


	# len_char = feature_extracter.get_textlength()
	# # word_unique = feature_extracter.word_counter()
	# # sent = feature_extracter.sentence_counter()
	# # ari_score = feature_extracter.ari_score()
	# outcomes = feature_extracter.outcome_variable()
	# stars = feature_extracter.review_stars()

	# outcomes_1, stars_1 = ids, other = zip(*((id1, other) for id1, other in zip(outcomes, stars) if other == 1))
	# outcomes_5, stars_5 = ids, other = zip(*((id1, other) for id1, other in zip(outcomes, stars) if other == 5))
	# plot.show_histogram(outcomes, 'upvotes/total votes', "Count")
	# plot.show_scatter_plot(outcomes, [len_char[r][0] for r in len_char])
	# plot.show_histogram(outcomes_1, 'upvotes/total votes', "Count of 1 star rating")
	# plot.show_histogram(outcomes_5, 'upvotes/total votes', "Count of 1 star rating")


	# print "parsed!"
	text_features = feature_extracter.get_features_concat()
	bag_of_words_features = feature_extracter.bag_of_words()
	combined_features = np.concatenate((bag_of_words_features, text_features), axis = 1)
	print combined_features.shape
