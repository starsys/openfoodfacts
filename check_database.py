# coding: utf-8

from category import *
from tables import *
import os


class CheckDatabase:
    def __init__(self):
        # use of categories defined in categories.txt (openfoodfacts categories used for this project)
        with open(os.path.abspath(os.path.dirname(__file__)) + "/" + "categories.txt", "r") as f:
            category_list = f.read().splitlines()
        # Checking existing mysql tables
        database_tables = make_query("""SHOW TABLES;""")
        # comparison of existing tables with awaited necessary tables only
        if database_tables != [('category',), ('product',), ('substituted',)]:
            print("Base incohérente. Reconstruction....")
            Table()  # database rebuild
        else:
            print("Base existante OK")
        # line count of category and product tables
        nb_line_category = make_query("""SELECT COUNT(*) FROM category;""")
        nb_line_product = make_query("""SELECT COUNT(*) FROM product;""")
        sql_categories = make_query("""SELECT name FROM category;""")
        sql_cat = []
        # creation of a list containing the names of each category in the SQL "category" table
        for item in sql_categories:
            sql_cat.append(item[0])
        # checking if category or product tables are not empty or if the category.txt data is different \
        # from the existing SQL "category" table
        if nb_line_category[0] == (0,) or nb_line_product[0] == (0,) or set(sql_cat) != set(category_list):
            print("Au moins une table est vide ou incohérente, suppression puis remplissage des tables...")
            make_query("""DELETE FROM category;""", method="modify")
            make_query("""DELETE FROM product;""", method="modify")
            for category in category_list:
                Category(category)  # creation of SQL categories and products
        else:
            print("Les tables ne sont pas vides et correspondent aux données de 'categories.txt' OK")
        print("-------------------------------------------------------------------------------------------------------")
