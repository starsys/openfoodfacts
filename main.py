# coding: utf-8
""" This is the main program"""

from category import *
from tables import *
# from sql_requests import *
from terminal_interface import *
import os

# use of categories defined in categories.txt (openfoodfacts categories used for this project)
with open(os.path.abspath(os.path.dirname(__file__)) + "/" + "categories.txt", "r") as f:
    category_list = f.read().splitlines()
# Checking existing mysql tables
database_tables = make_query("""SHOW TABLES; SELECT %s""", ("",))
# comparison of existing tables with awaited necessary tables only
if database_tables != [('category',), ('product',), ('substituted',)]:
    print("Base incohérente. Reconstruction....")
    Table() # database rebuild
else:
    print("Base existante OK")
# line count of category and product tables
nb_line_category = make_query("""SELECT COUNT(*) FROM category; SELECT %s""", ("",))
nb_line_product = make_query("""SELECT COUNT(*) FROM product; SELECT %s""", ("",))

# checking if category or product tables are not empty or if a category is not missing
if nb_line_category[0] == (0,) or nb_line_product[0] == (0,) or nb_line_category[0][0] != len(category_list) :
    print("Au moins une table est vide, remplissage des tables...")
    for category in category_list:
        Category(category) #creation of SQL categories and products
else:
    print("Les tables ne sont pas vides. OK")
print("-------------------------------------------------------------------------------------------------------")
Terminal_interface() # display of user interface in terminal

