--A basic python api for indix--

Very basic use:
     import indix
     indix=IndixRestClient(app_id=your_app_id, app_key=your_app_key)

To search products by a query:
     response=indix.products(query="QUERY_GOES_HERE)

And to get the json from the response:
     response.json()

For now, you can figure out the rest from looking at the source code. It's only 84 lines long right now.
