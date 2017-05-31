import time
from yellow_page_api.YellowAPI import YellowAPI
from yellow_page_api.MerchantDetails import MerchantDetails
from search_relevance.search_relevance import SearchRelevance
import json
import click

@click.command()
@click.option('--name', prompt='The company name')
def get_merchant_categories(name):
    UID = '6k854ydrwq5nn3yx3qbwqrm7'

    api = YellowAPI(UID)
    api.set_places_api_key(UID)
    rep = json.loads(api.find_business(name, 'quebec').decode("UTF-8"))
    time.sleep(1)
    if len(rep['listings']) > 0:
        search_relevance = SearchRelevance(name)
        business_names = [x['name'] for x in rep['listings']]
        business_to_get = search_relevance.get_most_relevant_term(business_names)
        business_index = business_names.index(business_to_get)
        merchant_details = MerchantDetails(rep['listings'][business_index])
        listing_details = api.get_business_details(merchant_details.city, merchant_details.prov,
                                                   merchant_details.business_name, merchant_details.listing_id)
        categories_response = json.loads(listing_details.decode("UTF-8"))['categories']
        print("Results found for : %s" % merchant_details.business_name)
        print([x['name'] for x in categories_response])
    else:
        print("No company with the name %s were found" % name)

if __name__ == '__main__':
    get_merchant_categories()



