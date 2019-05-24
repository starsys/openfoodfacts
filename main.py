# coding: utf-8
""" This is the main program"""

from category import *
from tables import *

# print_sql("SELECT * FROM product", ())

Table()

category_list = ["cookies", "steaks", "nouilles", "snacks"]
# category_list = ["cookies", "steaks"]

for category in category_list:
    Category(category)




