import requests
import json
import os


class indixException(Exception):
    pass

class indixRestException(indixException):
    """ This should do something with error codes from indix. Maybe.

    :param int status: the error code
    :param str uri: the url
    :param str msg: the message, if one exists
    """
    def __init__(self, status, uri, msg=""):
        self.uri=uri
        self.status=status
        self.msg=msg

    def __str__(self):
        return "ERROR %s: %s (%s)" % (self.status, self.msg, self.uri)

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
    for key, value in kwargs.items():
        full_url = "%s%s=%s&" % (full_url, key, value)
    response = requests.get(full_url)
    return response

def pretty_print(json_to_print, sort_keys=True):
    print(json.dumps(json_to_print, sort_keys=sort_keys, indent=4, separators=(',', ': ')))


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
                raise indixException("""You need app_id and app_key when you initialize stuff,
                or add environment variables (see readme)""")

        self.base = base
        self.app_id, self.app_key = app_id, app_key
        self.version_uri = "%s/%s" % (base, version)

    def brands(self, query=None):
        """
        :param query: the brand you want to search for
        """
        response = make_request(self.version_uri, "brands", query=query,
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)
    
    def stores(self, query=None):
        """
        :param query: the stores you want to search for
        """
        response = make_request(self.version_uri, "stores", query=query,
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)

    def categories(self):
        """
        Takes not params.  Returns json for all possible catagories
        """
        response = make_request(self.version_uri, "categories",
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)

    def products(self, pageNumber=1, query="", storeId="", brandId="", categoryId="",
                 startPrice="", endPrice="", sortBy="", priceHistoryAvail=False):
        """
        :param int pageNumber: page number to get
        :param query: product to search for
        :param storeId: storeId, form indix.stores
        :param brandId: brandId, from indix.brands
        :param categoryId: categoryId, from indix.categories
        :param startPrice: low price
        :param endPrice: high price
        :sortBy: must be one of: "RELEVANCE", "PRICE_LOW_TO_HIGH", "PRICE_HIGH_TO_LOW", "MOST_RECENT"
        or blank
        :priceHistoryAvail bool: if True, will only return products with price history available
        Returns: json for 10 products, dependent on the page you choose
        """
        response = make_request(self.version_uri, "products", pageNumber=pageNumber, query=query,
                                storeId=storeId, brandId=brandId, categoryId=categoryId,
                                startPrice=startPrice, endPrice=endPrice, sortBy=sortBy,
                                priceHisotryAvail=priceHistoryAvail,
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)

    def productById(self, id=None, pageNumber=1):
        """
        :param id: productId from indix.products
        :param pageNumber: page number
        Returns: JSON for correct page of that product
        """
        response = make_request(self.version_uri, "products/%s" % id, pageNumber=pageNumber,
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)

    def pricesById(self, id=None):
        """
        :param id: productId from indix.products
        Returns json for price history for an item
        """
        response = make_request(self.version_uri, "products/%s/prices" % id,
                                app_id=self.app_id, app_key=self.app_key)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)

    def raw(self, endpoint=None, **kwargs):
        """
        :param endpoint: the url to all to the end of api.indix.com/api/beta/
        :param **kwargs: dictionary of extra things to add to url as a GET request
        Returns: json
        """
        response = make_request(self.version_uri, endpoint,
                                app_id=self.app_id, app_key=self.app_key, **kwargs)
        if response.ok:
            return response
        else:
            raise indixRestException(response.status_code, response.url, response.reason)
