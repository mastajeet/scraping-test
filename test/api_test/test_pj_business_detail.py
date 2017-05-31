from yellow_page_api.MerchantDetails import MerchantDetails
import unittest
import json

class TestPJBusinessDetails(unittest.TestCase):

    listing = None

    def setUp(self):
        self.listing = json.load(open('./test/data/pj_listing.json'))

    def test_variables(self):
        details = MerchantDetails(self.listing)
        self.assertEqual('Québec',details.city)
        self.assertEqual('QC', details.prov)
        self.assertEqual('Restaurant Tomas Tam', details.business_name)
        self.assertEqual('8076842', details.listing_id)
