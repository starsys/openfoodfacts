# coding: utf-8

import requests
from product import *

class Category:

    def __init__(self, name):
        self.name = name
        self.url = "https://fr.openfoodfacts.org/categorie/"+self.name
        self.sql_category_id = 0
        self.fill_sql_table_category()
        self.generate_products_of_category()

    def fill_sql_table_category(self):
        make_query(""" INSERT INTO `category`
                                  (`name`, `url`) VALUES (%s,%s)""", (self.name, self.url), method = "insert")

    def generate_products_of_category(self):
        Product(self.name)


