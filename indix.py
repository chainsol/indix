import requests
import json
import os

sortBy_legal = ["RELEVANCE", "PRICE_LOW_TO_HIGH", "PRICE_HIGH_TO_LOW", "MOST_RECENT", ""]

def find_credentials():
    """Look in the current environment for indix account creds"""
    try:
        app_id = os.environ["INDIX_APP_ID"]
        app_key = os.environ["INDIX_APP_KEY"]
        return app_id, app_key
    except:
        return None, None

def make_request(base_uri, endpoint, **kwargs):
    full_url = "%s/%s/?" % (base_uri, endpoint)
    for key, value in kwargs.iteritems():
        full_url = "%s%s=%s&" % (full_url, key, value)
    response = requests.get(full_url)
    return response

def pretty_print(json_to_print, sort_keys=True):
    print json.dumps(json_to_print, sort_keys=sort_keys, indent=4, separators=(',', ': '))


class IndixRestClient(object):
    """
    A client for accessing the indix REST API

    :param str app_id: The app ID
    :param str app_key: The app key
    """

    def __init__(self, app_id=None, app_key=None, base="http://api.indix.com/api",
                 version="beta"):
        """Create a indix REST API client."""

        # Get account creds
        if not app_id or not app_key:
            app_id, app_key = find_credentials()
            if not app_id or not app_key:
                print "You need a app_id and app_key to work, you idiot."

        self.base = base
        self.app_id, self.app_key = app_id, app_key
        self.version_uri = "%s/%s" % (base, version)

    def brands(self, query=None):
        response = make_request(self.version_uri, "brands", query=query,
                                app_id=self.app_id, app_key=self.app_key)
        return response
        
    def stores(self, query=None):
        response = make_request(self.version_uri, "stores", query=query,
                                app_id=self.app_id, app_key=self.app_key)
        return response

    def catagories(self):
        response = make_request(self.version_uri, "categories",
                                app_id=self.app_id, app_key=self.app_key)
        return response

    def products(self, pageNumber=1, query="", storeId="", brandId="", categoryId="",
                 startPrice="", endPrice="", sortBy="", priceHistoryAvail=False):
        if sortBy not in sortBy_legal:
            print "sortBy must be a legal value, see the source for more"
            return -1
        response = make_request(self.version_uri, "products", pageNumber=pageNumber, query=query,
                                storeId=storeId, brandId=brandId, categoryId=categoryId,
                                startPrice=startPrice, endPrice=endPrice, sortBy=sortBy,
                                priceHisotryAvail=priceHistoryAvail,
                                app_id=self.app_id, app_key=self.app_key)
        return response

    def productById(self, id=None, pageNumber=1):
        response = make_request(self.version_uri, "products/%s" % id, pageNumber=pageNumber,
                                app_id=self.app_id, app_key=self.app_key)
        return response

    def pricesById(self, id=None):
        response = make_request(self.version_uri, "products/%s/prices" % id,
                                app_id=self.app_id, app_key=self.app_key)
        return response