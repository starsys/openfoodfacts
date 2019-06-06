# coding: utf-8

import mysql.connector
from config import *


def make_query(sql_query, param=None, method="select"):
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

        # insertion / deletion SQL request
        if method == "modify":
            connection.commit()
            print("Record modified successfully into table")

        # select SQL request
        if method == "select":
            result = cursor.fetchall()
            return result

    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occurred
        print("Failed inserting record into {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")
