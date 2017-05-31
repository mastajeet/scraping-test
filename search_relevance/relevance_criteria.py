from collections import Counter


class RelevanceCritera:
    def score(self, searched, found):
        pass

class MatchingLettersOccurence(RelevanceCritera):

    def score(self, searched, found):
        searched_letter_occurence = Counter(searched)
        found_letter_occurence = Counter(found)
        matching_frequency = self._get_occurence_frequency(searched_letter_occurence, found_letter_occurence)
        return self._calculate_aggregate_score(matching_frequency)

    def _calculate_aggregate_score(self,letter_matching_frequency):
        aggregate_score = 0

        nb_letters = len(letter_matching_frequency)
        for _, frequency in letter_matching_frequency.items():
            aggregate_score += frequency/nb_letters

        return aggregate_score

    def _get_occurence_frequency(self, searched_occurence, found_occurence):
        matching_occurence_frequency = {}
        for searched_letter, searched_letter_occurence in searched_occurence.items():
            found_frequency = 0
            if searched_letter in found_occurence.keys():
                found_frequency = self._calculate_search_to_found_letter_frequency(searched_letter_occurence,
                                                                                  found_occurence[searched_letter])
            matching_occurence_frequency[searched_letter] = found_frequency

        return matching_occurence_frequency

    @staticmethod
    def _calculate_search_to_found_letter_frequency(searched_letter_occurence, found_letter_occurence):
        found_frequency = found_letter_occurence / searched_letter_occurence
        found_frequency = min(1, found_frequency)
        return found_frequency
