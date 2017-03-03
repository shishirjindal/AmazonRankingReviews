import features
import get_data
import plot

if __name__ == '__main__':

    data_getter = get_data.Get_Data()
    data_reviews = data_getter.parse("./filtered_reviews")

    # print "parsed!"
    # bow = Bag_of_words(data_reviews)
    # clean_train_reviews = bow.gen_bag_for_all()

    # features = bow.train_bag(clean_train_reviews)

    plot.render(data_reviews)
    # feature_extracter = features.Extract_Features(data_reviews)
    # len_char = feature_extracter.get_textlength()
    # word_unique = feature_extracter.word_counter()
    # sent = feature_extracter.sentence_counter()
    # ari_score = feature_extracter.ari_score()

