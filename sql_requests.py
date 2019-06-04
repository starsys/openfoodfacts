# coding: utf-8

import mysql.connector
from config import *


def make_simple_query(sql_query, method="delete"):
    try:
        connection = mysql.connector.connect(host=HOST,
                                             database=DATABASE,
                                             user=USER,
                                             password=PASSWORD)
        cursor = connection.cursor()
        cursor.execute(sql_query)

        # tables creation SQL request
        if method == "creation":
            print("Instruction successful")

        # insertion SQL request
        if method == "delete":
            connection.commit()
            print("Record inserted successfully into table")

        # select SQL request
        if method == "select":
            result = cursor.fetchall()
            # print("SELECT instruction OK")
            return result

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def make_query(sql_query, param, method="select"):
    try:
        connection = mysql.connector.connect(host=HOST,
                                             database=DATABASE,
                                             user=USER,
                                             password=PASSWORD)
        cursor = connection.cursor()
        cursor.execute(sql_query, param)

        # tables creation SQL request
        if method == "creation":
            print("Instruction successful")

        # insertion SQL request
        if method == "insert":
            connection.commit()
            print("Record inserted successfully into table")

        # select SQL request
        if method == "select":
            result = cursor.fetchall()
            # print("SELECT instruction OK")
            return result

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")
