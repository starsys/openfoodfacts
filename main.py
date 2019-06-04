# coding: utf-8
""" This is the main program"""

from check_database import *
from terminal_interface import *

CheckDatabase()  # check if tables "category", "product" and "substituted" are already existing and correspond \
# to the content of "categories.txt". If not or if data is corrupted, tables are created / filled correctly
TerminalInterface()  # display of user interface in terminal
