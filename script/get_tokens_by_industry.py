import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import




# companies doit etre un dictionnaire
#  names : nom de la compagnie
#  Industry : nom de l'industrie
#  Products: nom des produits de la compagnie

# obsolete
def concatenate_industry_words(companies):
    industries = get_industries(companies)

    for industry in industries:
        total_industry_texts = []
        for company in [x for x in companies if 'Industry' in x and x['Industry'] == industry]:
            total_industry_texts.append(company['words'])
            if 'Products' in company:
                total_industry_texts.append(company['Products'])

    return total_industry_texts

def get_industries(companies):
    return set([x['Industry'] for x in companies if 'Industry' in x])

def get_fitted_vectorizer(bunch):
    vectorizer = CountVectorizer(token_pattern="[a-zA-Z]+")
    fit = vectorizer.fit_transform(bunch['data'])
    return vectorizer,fit

def convert_companies_to_bunchlike(companies):
    bunch = generate_bunchlike()

    for company in [x for x in companies if 'Industry' in x]:
        if company['Industry'] not in bunch['industry_index'].keys():
            bunch['industry_index'][company['Industry']] = len(bunch['industry_index'])

        if 'words' in company:
            bunch['data'].append(company['words'])  if 'words' in company else False
            bunch['target_name'].append(company['Industry'])
            bunch['target'].append(bunch['industry_index'][company['Industry']])
        if 'Products' in company:
            bunch['data'].append(company['Products']) if 'Products' in company else False
            bunch['target_name'].append(company['Industry'])
            bunch['target'].append(bunch['industry_index'][company['Industry']])

    bunch['industry'] = dict((v, k) for k, v in bunch['industry_index'].items())

    return bunch

def generate_bunchlike():
    bunch = {}
    bunch['data'] = []
    bunch['target_name'] = []
    bunch['target'] = []
    bunch['industry_index'] = {}
    bunch['industry'] = {}
    return bunch

def convert_industry_to_bunchlike(industries):
    bunch = generate_bunchlike()

    for industry in industries:
        bunch['industry_index'][industry['Industry']] = len(bunch['industry_index'])

        if 'words' in industry:
            bunch['data'].append(industry['words'])
            bunch['target_name'].append(industry['Industry'])
            bunch['target'].append(bunch['industry_index'][industry['Industry']])

    bunch['industry'] = dict((v, k) for k, v in bunch['industry_index'].items())
    return bunch

def get_transformer_and_occurences(fit):
    tf_transformer = TfidfTransformer(use_idf=False).fit(fit)
    fitted = tf_transformer.transform(fit)
    return tf_transformer, fitted


def get_words_distribution(vectorizer, fitted):

    train_data_features = fitted.toarray()
    vocab = vectorizer.get_feature_names()
    dist = np.sum(train_data_features, axis=0)
    ngram_freq = {}

    # For each, print the vocabulary word and the frequency
    for tag, count in zip(vocab, dist):
        print(tag, count)
        ngram_freq[tag] = count

def remove_duplicated_industries(crawler_output):
    output = []
    for page in crawler_output:
        industries = [x['Industry'] for x in output]
        if page['Industry'] not in industries:
            output.append(page)
    return output
