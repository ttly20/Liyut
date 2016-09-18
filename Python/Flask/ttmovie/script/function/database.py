# coding=uft-8
'''
This is the class of the operation database.
Class name:Database

 Construction method:__init__()
 Prototype method:
 def __init__(self, localhost, username, password, database)
 The function of construction method is to create a database object and
a database operate.
 It throws a database link exception when it encounters an exception:
    MySQLdb.Error

method:operate()
 Prototype method:
 def _operate(self, str)
 The function of the method is to operate the database.
 It returns the result of the execution of the database operation or th-
rows a database operation exception when an exception is encountered:
    MySQLdb.Error
'''

import MySQLdb as mdb


class Database:

    def __init__(self, localhost, username, password, database):
        try:
            self.con = mdb.connection(localhost, username, password, /
                                      database)
            self.cur = con.cursor()
        except mdb.Error, e:
            return e

    def _operate(self, str):
        try:
            return self.cur.execute(str)
        except mdb.Error, e:
            return e

    def sentence(self, *str):
        try:
            if str[0] == "join":
                sql = "insert into usr (" + str(str[1]) + "," + str[2]/
                + "," + str[3] + "," + str[4] + "," + str[5] + ") "/
                 + "values (" + str[6] + "," + str[7] + "," + str[8]/
                 + "," + str[9] + "," + str[10] + " );"
            elif str[0] == "":
