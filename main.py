# coding: utf-8
""" This is the main program"""

from category import *

category_list = ["cookies", "steaks", "nouilles", "snacks"]
# category_list = ["cookies", "steaks"]

for category in category_list:
    instance_cat = Category(category)
    instance_cat.fill_sql_table_category()
    instance_cat.find_sql_category_id()
    instance_cat.generate_products_of_category()




