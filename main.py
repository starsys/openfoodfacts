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




def print_sql():
    choice1 = ""
    loop1 = 0
    choice2 = ""
    loop2 = 0
    choice3 = ""
    loop3 = 0
    print("Ce programme vous propose de substituer un aliment par un équivalent plus sain. Voici les catégories que vous pouvez parcourir : \n")
    id_category = []
    id_product = []
    id_substituted = []
    # for row in make_query("SELECT * FROM category; SELECT %s", ("", )):
    #     print("ID:", row[0], "|", row[1])
    #     id_category.append(row[0])
    # print("")
    # choice1 = input("Veuillez choisir une catégorie en saisissant son ID puis entrée : ")
    # print("-------------------------------------------------------------------------------------------------------")
    while not choice1.isdigit() or int(choice1) not in id_category:
        if loop1 != 0:
            print("Veuillez saisir un identifiant existant ! \n")
        for row in make_query("SELECT * FROM category; SELECT %s", ("",)):
            print("ID:", row[0], "|", row[1])
            if loop1 == 0:
                id_category.append(row[0])
        loop1 += 1
        print("")
        choice1 = input("Veuillez choisir une catégorie en saisissant son ID puis entrée : ")

    category_name = make_query("SELECT name FROM category WHERE id = %s", (choice1,))[0][0]

    while not choice2.isdigit() or int(choice2) not in id_product:
        if loop2 != 0:
            print("Veuillez saisir un identifiant existant ! \n")
        for row in make_query("SELECT * FROM product WHERE category_ID = %s", (choice1,)):
            print("ID:", row[0], "|", row[1])
            if loop2 == 0:
                id_product.append(row[0])
        loop2 += 1
        print("")
        choice2 = input("Veuillez choisir un produit à substituer en saisissant son ID puis entrée : ")

    nutrition_grade_selected_product = make_query("SELECT nutrition_grades FROM product WHERE id = %s", (choice2,))[0][0]

    product_name = make_query("SELECT name FROM product WHERE id = %s", (choice2,))[0][0]
    if not make_query("SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s",
                          (nutrition_grade_selected_product, choice1)):
        print("Il n'existe pas de produit plus sain que", product_name, " dans la catégorie", category_name)
    else:
        print("Vous pourriez remplacer cet aliment par : \n")

        while choice3 != "q" and (not choice3.isdigit() or int(choice3) not in id_substituted):
            if loop3 != 0:
                print("Veuillez saisir un identifiant existant ! \n")
            for row in make_query("SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s", (nutrition_grade_selected_product, choice1)):
                print("ID:", row[0], "|", row[1], "|", "Description : ", row[5], "|", row[4], "|", row[6])
                if loop3 == 0:
                    id_substituted.append(row[0])
            loop3 += 1
            print("")
            choice3 = input("Si vous souhaitez enregistrer l'un de ces produit en substitution de " + product_name + ", tapez son ID, sinon, tapez 'q' pour quitter : ")
        if choice3 == "q":
            print("Au revoir")
        else:
            substituted_name = make_query("SELECT name FROM product WHERE id = %s", (choice3,))[0][0]
            print(substituted_name)

print_sql()
