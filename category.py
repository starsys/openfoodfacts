# coding: utf-8

import requests
from sql_requests import *


class Category:

    def __init__(self, name):
        self.name = name
        self.url = "https://fr.openfoodfacts.org/categorie/"+self.name
        self.json = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0="+self.name+"&tagtype_1=languages&tag_contains_1=contains&tag_1=fr&page_size=20&search_simple=1&action=process&json=1").json()
        self.sql_category_id = 0
        self.fill_sql_table_category()
        self.find_sql_category_id()
        self.generate_products_of_category()

    def find_sql_category_id(self):
        self.sql_category_id = make_query("SELECT id FROM category WHERE name=%s", (self.name,))[0][0]
        print(self.sql_category_id)
        # self.sql_category_id = sql_select("SELECT id FROM category ORDER BY id DESC LIMIT 1", ())
        # self.sql_category_id = sql_select("SELECT MAX(id) FROM category")




    def generate_products_of_category(self):
        for value in (self.json["products"]):
            if "nutrition_grades" in value and "product_name_fr" in value and "generic_name" in value and "url" in value and value["nutrition_grades"] in ["a","b","c","d","e"] and value["product_name_fr"] != "" and "\n" not in value["product_name_fr"] and value["generic_name_fr"] != "":
                if value["stores"]:
                    store = "Disponible à " + value["stores"]
                else:
                    store = "Aucun magasin ne propose ce produit"

                make_query(""" INSERT INTO `product`
                                                      (`name`, `category_ID`,`nutrition_grades`, `store`, `description`, `url`) VALUES (%s,%s,%s,%s,%s,%s)""",
                            (value['product_name_fr'], self.sql_category_id, value["nutrition_grades"], store,
                             value["generic_name"], value["url"]), method = "insert")


    def fill_sql_table_category(self):
        make_query(""" INSERT INTO `category`
                                  (`name`, `url`) VALUES (%s,%s)""", (self.name, self.url), method = "insert")

