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

    
