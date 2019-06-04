# coding: utf-8

from sql_requests import *

#############################################################################
#This class create "P5" Database and [Category, Product, Substituted] tables#
#############################################################################


class Table:

    def __init__(self):
        make_simple_query("""
            DROP DATABASE IF EXISTS p5;
            CREATE DATABASE p5 CHARACTER SET 'utf8';
            USE p5;
            CREATE TABLE Category (
                id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                url VARCHAR(100) NOT NULL,
                PRIMARY KEY (id)
            )
            ENGINE=INNODB DEFAULT CHARSET=utf8;
            CREATE TABLE Product (
                id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                category_ID SMALLINT UNSIGNED NOT NULL,
                nutrition_grades VARCHAR(1) NOT NULL,
                store VARCHAR(100),
                description VARCHAR(1000) NOT NULL,
                url VARCHAR(1000) NOT NULL,
                CONSTRAINT fk_product_category_ID FOREIGN KEY (category_ID) REFERENCES category(id) ON DELETE CASCADE
            )
            ENGINE=INNODB DEFAULT CHARSET=utf8;
            CREATE TABLE Substituted (
                id SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                original_product_ID SMALLINT UNSIGNED NOT NULL,
                substituted_product_ID SMALLINT UNSIGNED NOT NULL,
                CONSTRAINT fk_original_product_ID FOREIGN KEY (original_product_ID) REFERENCES product(id) ON DELETE CASCADE,
                CONSTRAINT fk_substituted_product_ID FOREIGN KEY (substituted_product_ID) REFERENCES product(id) ON DELETE CASCADE
            )
            ENGINE=INNODB DEFAULT CHARSET=utf8;
            """, method = "creation")
