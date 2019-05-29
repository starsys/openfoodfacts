# coding: utf-8
""" This is the main program"""

from category import *
from tables import *
from sql_requests import *
from pprint import *


# Table()
#
# # category_list = ["cookies", "steaks", "nouilles", "snacks"]
# category_list = ["cookies", "steaks"]
#
# for category in category_list:
#     Category(category)


def user_menu(input_text, query, param, presentation = "short"):
    choice = ""
    id_list = []
    loop = 0
    while choice != "q" and (not choice.isdigit() or int(choice) not in id_list):
        if loop != 0:
            print("Veuillez saisir un identifiant existant ! \n")
        for row in make_query(query, param):
            if presentation == "short":
                print("ID:", row[0], "|", row[1])
            else:
                print("ID:", row[0], "|", row[1], "|", "Description : ", row[5], "|", row[4], "|", row[6])
            if loop == 0:
                id_list.append(row[0])
        loop += 1
        choice = input("\n" + input_text)
        print("-------------------------------------------------------------------------------------------------------")
    if choice == "q":
        print("Au revoir")
    return choice


def print_sql():
    print("Ce programme vous propose de substituer un aliment par un équivalent plus sain. Voici les catégories que vous pouvez parcourir : \n")
    choice1 = user_menu("Veuillez choisir une catégorie en saisissant son ID puis entrée : ", "SELECT * FROM category; SELECT %s", ("",))

    category_name = make_query("SELECT name FROM category WHERE id = %s", (choice1,))[0][0]

    choice2 = user_menu("Veuillez choisir un produit à substituer en saisissant son ID puis entrée : ", "SELECT * FROM product WHERE category_ID = %s", (choice1,), "long")

    nutrition_grade_selected_product = make_query("SELECT nutrition_grades FROM product WHERE id = %s", (choice2,))[0][0]

    product_name = make_query("SELECT name FROM product WHERE id = %s", (choice2,))[0][0]
    if not make_query("SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s",
                          (nutrition_grade_selected_product, choice1)):
        print("Il n'existe pas de produit plus sain que", product_name, " dans la catégorie", category_name)
    else:
        print("Vous pourriez remplacer cet aliment par : \n")

        choice3 = user_menu("Si vous souhaitez enregistrer l'un de ces produit en substitution, tapez son ID, sinon, tapez 'q' pour quitter : ", "SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s", (nutrition_grade_selected_product, choice1), "long")
    if choice3 != "q":
        substituted_name = make_query("SELECT name FROM product WHERE id = %s", (choice3,))[0][0]
        print(substituted_name)

print_sql()
