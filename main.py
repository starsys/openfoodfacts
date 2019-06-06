# coding: utf-8

from check_database import *
from terminal_interface import *


if __name__ == '__main__':
    CheckDatabase()  # check if tables "category", "product" and "substituted" are already existing and correspond \
    # to the content of "categories.txt". If not or if data is corrupted, tables are created / filled correctly
    TerminalInterface().print_sql()  # display of user interface in terminal

