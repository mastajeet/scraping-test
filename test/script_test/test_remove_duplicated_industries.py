import unittest
from script.get_tokens_by_industry import remove_duplicated_industries
class TestRemoveDuplicatedIndustries(unittest.TestCase):


    def test_table_with_duplicated(self):
        documents = [{'Industry':'a','words':'foo'},{'Industry':'a','words':'foo'},{'Industry':'b','words':'bar'}]
        documents_without_duplicated =remove_duplicated_industries(documents)
        self.assertEqual(2,len(documents_without_duplicated))

    def test_table_without_duplicate(self):
            documents = [{'Industry': 'a', 'words': 'foo'}, {'Industry': 'b', 'words': 'bar'}]
            documents_without_duplicated = remove_duplicated_industries(documents)
            self.assertEqual(2, len(documents_without_duplicated))

