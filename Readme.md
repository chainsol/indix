#A basic python api for [indix](http://indxi.com)

Requires:

     python2.7, python3.3, or pypy2.7 with [requests](http://docs.python-requests.org/en/latest/index.html) library
     Untested on pypy3.3.

Very basic use:

      from indix import IndixRestClient
      indix=IndixRestClient(app_id=your_app_id, app_key=your_app_key)

To search products by a query:

      response=indix.products(query="QUERY_GOES_HERE")

Other fucntions include:

      indix.brands(query="brand_name")                # Brands
      indix.stores(query="store_name")                # Stores
      indix.categories()                              # Lists all available catagories
      indix.productById(id="productId",pageNumber=1)  # Gets $page_number of $id
      indix.pricesById(id="id")                       # Gets historical prices for item with $id

And the rest of the options for `indix.products`:

    int pageNumber:     page number to get
    string query:       what to search for
    string storeId:     storeId from indix.stores
    string brandId:     brandId from indix.brands
    string categoryId:  categoryId from indix.categroies
    float startPrice:   Low price to search for
    float endPrice:     High price to search for
    priceHistoryAvail:  if True, will only return products with price history available
    sortBy:             one of "RELEVANCE", "PRICE_LOW_TO_HIGH", "PRICE_HIGH_TO_LOW", "MOST_RECENT", or blank

To get the json from the response:

     response.json()

(With pypy is seems to be necessary to remove the `()`, ie `response.json`

I also included a small function to make pretty printing easier:

      from indix import pretty_print
      pretty_print(response.json())


You can also set the app_id (`INDIX_APP_ID`) and app_key (`INDIX_APP_KEY`) as environment variables, and python will (should) see them.


If you have any questions, feel free to contact me at <matthew@mtbentley.us>.  
Please use the issues tracker for any bugs or feature requests.  
And as always, please feel free to submit patches.  
