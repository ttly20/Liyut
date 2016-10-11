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

method:_sentedelect(),_senteinsert(),_senteselect(),_senteupdate()
 Prototype method:
  def _senteSelect(self, tab, str)
  def _senteInsert(self, str, tab)
  def _senteUpdate(self, *str, tab, qualifiction)
  def _senteDelect(self, tab, qualifiction)
 Statement combination:select\delect\insert\update
 The method return sql statement string

method:_senteSafe()
 Prototype method:
  def _senteSafe(self, str)
 This method is to do security checks
 This method returns an exception when it detects a SQL statement security problem,or does nothing:
 safeErerr
'''

import MySQLdb as mdb
import re


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

    def _senteSafe(self, str):
        try:
            sqlRe = re.compile(r"\bselect|updata|insert|delect|alter|exec\b"
                        , re.I)
            sqlQualifi = re.compile(r'\bwhere|values|from|like|into|set\b'
                        , re.I)
            if sqlRe.search(str) != None:
                if sqlQualifi.search(str) != None:
                    raise "safeErerr", str
        except "safeErerr":
            return "safe ererr:" + e.args
    def _senteSelect(self, tab, str):
        sqlStr = "select " + str + " from " + tab
        return sqlStr
    def _senteInsert(self, str, tab):
        sqlStr = "insert into " + tab + "(" + str.keys() + ") values ("
        sqlStr += str.values() + ")"
        return sqlStr
    def _senteUpdate(self, *str, tab, qualifiction):
        sqlStr = "update " + tab + " set (" + str + ")"
        if qualifiction != "":
            sqlStr += " where " + qualifiction
        return sqlStr
    def _senteDelect(self, tab, qualifiction):
        sqlStr = "delect from " + tab + " where " + qualifiction
        return sqlStr
    def Database(self, qualifiction, values, key,):
