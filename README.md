# openfoodfacts
P5 Openclassrooms : "Utilisez les données publiques de l'OpenFoodFacts"

## Specifications
### User story description:

User has following choices on terminal:

1. Find my substituted foods.
1. Which food would you like to substitute ?
User choose option "1"
 
System asks following questions to be answered by user:

* Please select a category (several options identified by a number). User type chosen number (corresponding to wanted category) and press "enter".
    * Please select food (several options identified by a number). User type chosen number (corresponding to wanted food) and press "enter".
    
System propose a substitute of chosen food, its description, where to buy it (if available) and a description link.
User may choose to save this substitute in database.

 
### Functionalities


* Food search in Openfoodfacts database.
* User interact with system in terminal
* If user type unexpected character (anything other than a number), system will ask the question again.
* Search is applied on a Mysql database.

### Requirements
You need to create a config.py file (at the root) with your Mysql database credentials like this template:  
  

HOST='ip_address_of_the_mysql_server'  
DATABASE='database_name'  
USER='your_user'  
PASSWORD='your_password'

### Openfoodfacts API request parameters
![Openfoodfacts API request parameters](API_query_parameters.JPG)

### Program description
This program is working with a "P5" Mysql database with "category", "product", and "substituted" tables.
User must specify the food categories (existing in openfoodfacts) he wants to explore in: "categories.txt"

1. The program checks if the database contains expected tables. If not, existing database is erased and rebuild
1. The program fill the "category" table based on "categories.txt"
1. The program checks if tables are not empty and if the content of the table "category" reflect "categories.txt". If not, existing tables are erased and rebuild.
1. The programm fill the product table (after checking if expected data is available and meet standard) based on openfoodfacts API request
1. The program provide a user interface in terminal to let user browse categories / product and decide if he wants to record any substitution in "substituted" table.

    
