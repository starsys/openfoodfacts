# coding: utf-8
""" This is the main program"""

import requests
import json

data_cookies = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0=Cookies&tagtype_1=languages&tag_contains_1=contains&tag_1=fr&page_size=20&search_simple=1&action=process&json=1").json()
for index, value in enumerate(data_cookies["products"]):
    print(index, value['product_name_fr'])


