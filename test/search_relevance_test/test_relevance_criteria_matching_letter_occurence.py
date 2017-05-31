import unittest
import json
from os.path import join
from search_relevance.relevance_criteria import MatchingLettersOccurence


class TestRelevanceCriteriaMatchingLetterOccurence(unittest.TestCase):
    relevance_criteria = None
    searched_letter_occurence = None
    found_letter_occurence = None
    occurence_frequency = None
    searched_word = None
    found_word = None

    def setUp(self):
        self.relevance_criteria = MatchingLettersOccurence()
        test_data_path = './test/data/search_relevance'

        self.searched_letter_occurence = json.load(open(join(test_data_path, 'searched_letter_occurence.json')))
        self.found_letter_occurence = json.load(open(join(test_data_path, 'found_letter_occurence.json')))
        self.occurence_frequency = json.load(
            open(join(test_data_path, 'matching_letter_occurence_occurence_frequency.json')))
        self.searched_word = json.load(open(join(test_data_path, 'searched_word.json')))
        self.found_word = json.load(open(join(test_data_path, 'found_words.json')))

    def test_calculate_aggregate_score(self):
        aggregate_score = self.relevance_criteria._calculate_aggregate_score(self.occurence_frequency)
        self.assertAlmostEqual(0.625, aggregate_score)

    def test_calculate_search_to_found_letter_frequency_exactly_1(self):
        frequency = MatchingLettersOccurence._calculate_search_to_found_letter_frequency(
            self.searched_letter_occurence['a'],
            self.found_letter_occurence['a'],
        )
        self.assertAlmostEqual(1, frequency)

    def test_calculate_search_to_found_letter_frequency_bellow_1(self):
        frequency = MatchingLettersOccurence._calculate_search_to_found_letter_frequency(
            self.searched_letter_occurence['b'],
            self.found_letter_occurence['b'],
        )
        self.assertAlmostEqual(2 / 3, frequency)

    def test_get_occurence_frequency(self):
        occurence_frequency = self.relevance_criteria._get_occurence_frequency(self.searched_letter_occurence,
                                                                               self.found_letter_occurence)
        self.assertAlmostEqual(1,occurence_frequency['a'])
        self.assertAlmostEqual(2/3, occurence_frequency['b'])
        self.assertAlmostEqual(0, occurence_frequency['c'])
        self.assertRaises(KeyError, lambda: occurence_frequency['d'])

    def test_score(self):
        score = self.relevance_criteria.score(self.searched_word[0],self.found_word[0])
        self.assertAlmostEqual(2/3,score)
