class MerchantDetails:

    city = None
    prov = None
    business_name = None
    listing_id = None

    def __init__(self,listing):
        address = listing['address']
        self.city = address['city']
        self.prov = address['prov']
        self.business_name = listing['name']
        self.listing_id = listing['id']

