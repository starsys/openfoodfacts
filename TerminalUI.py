# coding: utf-8

from substituted import *


class TerminalUI:

    def user_menu(self, input_text, query, param, presentation="short"):
        choice = ""
        id_list = []
        loop = 0
        while choice != "q" and (not choice.isdigit() or int(choice) not in id_list):
            # check if input is a digit and correspond to an existing ID. Other inputs will be denied
            if loop != 0:  # Warning of incorrect input not displayed at first round
                print("Veuillez saisir un identifiant existant ! \n")
            for row in make_query(query, param):
                if presentation == "short":
                    print("ID:", row[0], "|", row[1])  # Only first 2 columns (ID and Name) will be shown (for category)
                else:
                    print("ID:", row[0], "|", row[1], "|", "Description : ", row[5], "|", row[4], "|", row[6])
                    # All columns (from product table) will be shown
                if loop == 0:
                    id_list.append(row[0])  # List of all choosable IDs is built during first loop only
            loop += 1
            choice = input("\n" + input_text)
            print("-----------------------------------------------------------------------------------------------\
--------")
        if choice == "q":
            print("Au revoir")
            exit()
        return choice

    def print_sql(self):
        choice_substituted = "q"
        view_substituted = input("Souhaitez vous visualiser les produits que vous avez déjà substitué ? o/n \n")
        if view_substituted == "o":
            self.print_substituted() # print all already existing substituted products
        print("Ce programme vous propose de substituer un aliment par un équivalent plus sain. "
              "Voici les catégories que vous pouvez parcourir : \n")
        # ID of chosen category
        choice_category = self.user_menu("Veuillez choisir une catégorie en saisissant son ID puis entrée : ",
                                         "SELECT * FROM category; SELECT %s", ("",))
        # Name corresponding to category ID
        category_name = make_query("SELECT name FROM category WHERE id = %s", (choice_category,))[0][0]
        # ID of chosen product
        choice_product = self.user_menu("Veuillez choisir un produit à substituer en saisissant son ID puis entrée : ",
                                        "SELECT * FROM product WHERE category_ID = %s", (choice_category,), "long")

        nutrition_grade_selected_product = make_query("SELECT nutrition_grades FROM product WHERE id = %s",
                                                      (choice_product,))[0][0]
        # Name corresponding to product ID
        product_name = make_query("SELECT name FROM product WHERE id = %s", (choice_product,))[0][0]
        # If no product with better nutrition_grade from the same category exist :
        if not make_query("SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s",
                          (nutrition_grade_selected_product, choice_category)):
            print("Il n'existe pas de produit plus sain que", product_name, " dans la catégorie", category_name)
        else:
            print("Vous pourriez remplacer cet aliment par : \n")
            # Product ID from product in the same category with better nutrition_grade
            choice_substituted = self.user_menu("Si vous souhaitez enregistrer l'un de ces produit en substitution,"
                                                " tapez son ID, sinon, tapez 'q' pour quitter : ",
                                              "SELECT * FROM product WHERE nutrition_grades < %s AND category_ID = %s",
                                                (nutrition_grade_selected_product, choice_category), "long")
        if choice_substituted != "q":
            # Insertion of original_product_ID and substituted_product_id in table substituted
            Substituted(choice_product, choice_substituted)
            print("Si elle n'existait pas, cette substitution a bien été enregistrée en base de données")

    def print_substituted(self): # This method will display the content of substituted table
        # get all tuples (original_product_ID, substituted_product_id) from substituted table
        for couple in make_query("SELECT original_product_ID, substituted_product_ID FROM substituted",
                                        method="select"):
            # Find name of original_product_id
            original_name = make_query("SELECT name FROM product WHERE id = %s", (couple[0],), method="select")[0][0]
            # Find information from substituted product
            substituted_data = make_query("SELECT name, description, store, url FROM product WHERE id = %s",
                                          (couple[1],), method="select")[0]
            print("\"" + original_name + "\"" + " a été remplacé par " + "\"" + substituted_data[0] + "\"" + " "
                  + substituted_data[1] + " " + substituted_data[2] + " " + substituted_data[3])
        print("-------------------------------------------------------------------------------------------------------")
