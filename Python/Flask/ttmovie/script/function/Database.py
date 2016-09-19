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
            self.con = mdb.connection(localhost, username, password, \
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
                sql = "insert into usr (" + str(str[1]) + "," + str[2]\
                + "," + str[3] + "," + str[4] + "," + str[5] + ") "\
                + "values (" + str[6] + "," + str[7] + "," + str[8]\
                + "," + str[9] + "," + str[10] + " );"
            elif str[0] == "publish":
                sql = "insert into movie (" + str[1] + "," + str[2]\
                + "," + str[3] + "," + str[4] + "," + str[5] + ") "\
                + "," + str[6] + "," + str[7] + "," + str[8]\
                + "," + str[9] + "values" + str[10] + "," + str[11] \
                + "," + str[12] + "," + str[13] + "," + str[14] + ","\
                + str[15] + "," + str[16] + "," + str[17] + "," +\
                str[18] + " );"
            if str[0] == "revise":
                sql_str = "update " + str[2] + "set "
                sql_str1 = ""
                i = 3
                while i < str[1] + 1:
                    sql_str1 = sql_str1 + str[i] + "='" + str[i + 1] + "'"
                    if i < str[1] - 1:
                        sql_str1 = sql_str1 + ","
                        i = i + 2
                    sql = sql_str + " " + sql_str1 + " where " +\
                    str[len(str)-2] + "=" + str[len(str)-1]
            if str[0] == "inquire":
