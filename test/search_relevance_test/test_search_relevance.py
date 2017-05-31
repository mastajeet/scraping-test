import unittest
import json
from os.path import join
from search_relevance.search_relevance import SearchRelevance
from search_relevance.strictness_level import VeryLoose,MostStrict

class TestSearchRelevance(unittest.TestCase):
    searched_word = None
    found_words = None
    search_relevance = None

    def setUp(self):
        test_data_path = './test/data/search_relevance'
        self.searched_word = json.load(open(join(test_data_path, 'searched_word.json')))
        self.found_words = json.load(open(join(test_data_path, 'found_words.json')))
        self.search_relevance = SearchRelevance(self.searched_word[0])

    def test_load_relevant_criteria(self):
        self.search_relevance.relevance_criteria = []
        self.assertEqual(0, len(self.search_relevance.relevance_criteria))
        self.search_relevance._load_relevance_criteria()
        self.assertEqual(1, len(self.search_relevance.relevance_criteria))

    def test_set_strictness_level(self):
        self.search_relevance.set_strictness_level(VeryLoose())
        self.assertEqual(type(self.search_relevance.strictness_level),VeryLoose)


    def test_aggregate_score_over_criteria(self):
        score = self.search_relevance._aggregate_score_over_criteria(self.found_words[0])
        self.assertAlmostEqual(2 / 3, score)

    def test_get_most_relevant_score_and_term(self):
        score, term = self.search_relevance._get_most_relevant_score_and_term(self.found_words)
        self.assertAlmostEqual(0.83333333,score)
        self.assertEqual("aloah",term)

    def test_get_most_relevant_term(self):
        term = self.search_relevance.get_most_relevant_term(self.found_words)
        self.assertEqual("aloah", term)

    def test_get_most_relevant_term_none_found(self):
        self.search_relevance.set_strictness_level(MostStrict())
        term = self.search_relevance.get_most_relevant_term(self.found_words)
        self.assertIsNone(term)
