# coding: utf-8

import mysql.connector
from mysql.connector import errorcode

def sql_insert(sql_query, tuple):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='p5',
                                             user='root',
                                             password='Jestercapstarsys1')
        cursor = connection.cursor()
        cursor.execute(sql_query, tuple)
        connection.commit()
        print("Record inserted successfully into table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into {}".format(error))
    # closing database connection.

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def sql_select(sql_query, tuple):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='p5',
                                             user='root',
                                             password='Jestercapstarsys1')
        cursor = connection.cursor()
        cursor.execute(sql_query, tuple)
        result = cursor.fetchall()
        print("SELECT instruction OK")
        return result

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed to get record from database: {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")