# coding: utf-8
""" This is the main program"""

from category import *
from tables import *

Table()

category_list = ["cookies", "steaks", "nouilles", "snacks"]
# category_list = ["cookies", "steaks"]

for category in category_list:
    Category(category)




