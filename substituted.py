# coding: utf-8

from sql_requests import *


class Substituted:
    def __init__(self, original_product_ID, substituted_product_ID):
        make_query(""" INSERT INTO `substituted` (`original_product_ID`, `substituted_product_ID`) VALUES (%s,%s)""",
                             (original_product_ID, substituted_product_ID), method="insert")