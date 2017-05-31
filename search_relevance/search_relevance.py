from search_relevance.strictness_level import *
from search_relevance.relevance_criteria import *

class SearchRelevance():

    searched_term = None
    relevance_criteria = None
    strictness_level = Strict()

    def __init__(self, searched_terms):
        self.searched_term = searched_terms
        self._load_relevance_criteria()

    def _load_relevance_criteria(self):
        self.relevance_criteria = []
        self.relevance_criteria.append(MatchingLettersOccurence())

    def set_strictness_level(self,strictnesslevel):
        self.strictness_level = strictnesslevel

    def _get_most_relevant_score_and_term(self, found_terms):
        high_score = 0
        high_score_term = None

        for term in found_terms:
            aggregate_score = self._aggregate_score_over_criteria(term)
            if aggregate_score > high_score:
                high_score = aggregate_score
                high_score_term = term

        return high_score, high_score_term

    def get_most_relevant_term(self,found_terms):
        score, term = self._get_most_relevant_score_and_term(found_terms)
        if self.strictness_level.passes(score):
            return term
        else:
            return None

    def _aggregate_score_over_criteria(self, term):
        aggregate_score = 0
        for criteria in self.relevance_criteria:
            aggregate_score += criteria.score(self.searched_term,term)
        return aggregate_score


