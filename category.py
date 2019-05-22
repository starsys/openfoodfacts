# coding: utf-8

import requests
import mysql.connector
from mysql.connector import errorcode

class Category:

    def __init__(self, name):
        self.name = name
        self.url = "https://fr.openfoodfacts.org/categorie/"+self.name
        self.json = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=contains&tag_0="+self.name+"&tagtype_1=languages&tag_contains_1=contains&tag_1=fr&page_size=20&search_simple=1&action=process&json=1").json()
        self.sql_category_id = 0

    def find_sql_category_id(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='p5',
                                                 user='root',
                                                 password='Jestercapstarsys1')
            sql_insert_query = "SELECT id FROM category WHERE name=%s"
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, (self.name,))
            self.sql_category_id = cursor.fetchall()[0][0]

        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed to get record from database: {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def generate_products_of_category(self):
        store = ""
        for value in (self.json["products"]):
            if "nutrition_grades" in value and "product_name_fr" in value and "generic_name" in value and "url" in value and value["nutrition_grades"] in ["a","b","c","d","e"] and value["product_name_fr"] != "" and "\n" not in value["product_name_fr"] and value["generic_name_fr"] != "":
                if value["stores"]:
                    store = "Disponible à " + value["stores"]
                else:
                    store = "Aucun magasin ne propose ce produit"
                try:
                    connection = mysql.connector.connect(host='localhost',
                                                         database='p5',
                                                         user='root',
                                                         password='Jestercapstarsys1')
                    sql_insert_query = """ INSERT INTO `product`
                                              (`name`, `category_ID`,`nutrition_grades`, `store`, `description`, `url`) VALUES (%s,%s,%s,%s,%s,%s)"""
                    cursor = connection.cursor()
                    result = cursor.execute(sql_insert_query, (value['product_name_fr'], self.sql_category_id, value["nutrition_grades"], store, value["generic_name"], value["url"]))
                    connection.commit()
                    print("Record inserted successfully into python_users table")
                except mysql.connector.Error as error:
                    connection.rollback()  # rollback if any exception occured
                    print("Failed inserting record into {}".format(error))
                # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    def fill_sql_table_category(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='p5',
                                                 user='root',
                                                 password='Jestercapstarsys1')
            sql_insert_query = """ INSERT INTO `category`
                                  (`name`, `url`) VALUES (%s,%s)"""
            cursor = connection.cursor()
            result = cursor.execute(sql_insert_query, (self.name, self.url))
            connection.commit()
            print("Record inserted successfully into python_users table")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into table {}".format(error))
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

