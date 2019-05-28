# coding: utf-8

import requests
from sql_requests import *


class Product:
    def __init__(self, category_name):
        self.category_name = category_name
        self.name = ""
        self.sql_category_ID = 0
        self.nutrition_grades = ""
        self.url = ""
        self.description = ""
        self.store = ""
        self.json = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0="+self.category_name+"&tagtype_1=languages&tag_contains_1=contains&tag_1=fr&page_size=20&search_simple=1&action=process&json=1").json()
        self.find_sql_category_id()
        self.checkdata_for_sql_insertion()

    def find_sql_category_id(self):
        self.sql_category_id = make_query("SELECT id FROM category WHERE name=%s", (self.category_name,))[0][0]
        print("La categorie :" + " \"" + self.category_name + "\"" + " correspond à l'ID : " + str(self.sql_category_id) + " dans la table SQL")

    def checkdata_for_sql_insertion(self):
        for value in (self.json["products"]):
            if "nutrition_grades" in value and "product_name_fr" in value and "generic_name" in value and "url" in value and value["nutrition_grades"] in ["a","b","c","d","e"] and value["product_name_fr"] != "" and "\n" not in value["product_name_fr"] and value["generic_name_fr"] != "":
                self.name = value['product_name_fr']
                self.nutrition_grades = value["nutrition_grades"]
                self.url = value["url"]
                self.description = value["generic_name"]
                if value["stores"]:
                    self.store = "Disponible à " + value["stores"]
                else:
                    self.store = "Aucun magasin ne propose ce produit"

                make_query(""" INSERT INTO `product`
                                                      (`name`, `category_ID`,`nutrition_grades`, `store`, `description`, `url`) VALUES (%s,%s,%s,%s,%s,%s)""",
                            (value['product_name_fr'], self.sql_category_id, value["nutrition_grades"], self.store,
                             value["generic_name"], value["url"]), method = "insert")
