#A basic python api for indxi (indix.com)

Very basic use:

     import indix
     indix=IndixRestClient(app_id=your_app_id, app_key=your_app_key)

To search products by a query:

     response=indix.products(query="QUERY_GOES_HERE")

And to get the json from the response:

     response.json()

For now, you can figure out the rest from looking at the source code. It's only 84 lines long right now.

You can also set the app_id (`INDIX_APP_ID`) and app_key (`INDIX_APP_KEY`) as environment variables, and python will (should) see them.
