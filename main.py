from sklearn.datasets import fetch_20newsgroups
from script.get_tokens_by_industry import *

import json

###
# tests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

#
####

companies = json.load(open('result.json'))
test_data = json.load(open('test_data.json'))
companies = remove_duplicated_industries(companies)
bunch = convert_industry_to_bunchlike(companies)
industries = set(bunch['target_name'])

# categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
# twenty_train = fetch_20newsgroups(subset='train',
#     categories=categories, shuffle=True, random_state=42)
#
# train = {'data':twenty_train.data}
vectorizer, train_fit = get_fitted_vectorizer(bunch)
transformer, train_occurences = get_transformer_and_occurences(train_fit)

clf = MultinomialNB().fit(train_occurences, bunch['target'])

docs_new = ['house fee stock market', 'gaz petrol car ','expresso tea lemon']

X_new_counts = vectorizer.transform(docs_new)
# X_new_counts = vectorizer.transform([companies[0]['words']])
# X_new_counts = vectorizer.transform([test_data[0]['words']])
X_new_tfidf = transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (1, bunch['industry'][category]))


# get_words_distribution(vectorizer, train_fit)
