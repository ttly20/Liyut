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
  def _operate(self, string)
 The function of the method is to operate the database.
 It returns the result of the execution of the database operation or th-
rows a database operation exception when an exception is encountered:
    MySQLdb.Error

method:_sentedelect(),_senteinsert(),_senteselect(),_senteupdate()
 Prototype method:
  def _senteSelect(self, tab, dictdata)
  def _senteInsert(self, tab, dictdata)
  def _senteUpdate(self, tab, dictdata, qualifiction)
  def _senteDelect(self, tab, qualifiction)
 Statement combination:select\delect\insert\update
 The method return sql statement string

method:_senteSafe()
 Prototype method:
  def _senteSafe(self, string)
 This method is to do security checks
 This method returns an exception when it detects a SQL statement securi-
ty problem,or does nothing:
 True or False

method:op()
 Prototype method:
 def op(self, operation, tab, dictdata, quali = None)
 This method is used to perform security valida-
 tion and operation,The quali parameter is optional.

method:safe()
 Prototype method:
 def safe(self, string):
 This method is used to filter the irregular mysql characters

method:_dict2list()
 Prototype method:
 def _dict2list(self, dict, que)
 This method is used to convert a dictionary to a string
'''

import MySQLdb as mdb
import re


class Database:

    def __init__(self, localhost, username, password, database):
        """
        The function of construction method is to create a database object and
a database operate.
        It throws a database link exception when it encounters an exception:
    MySQLdb.Error
        """
        try:
            self.con = mdb.connection(localhost, username, password,
                                      database)
            self.cur = con.cursor()
        except mdb.Error, e:
            return e

    def safe(self, string):
        # This method is used to filter the irregular mysql characters
        return MySQLdb.escape_string(string)

    def _dict2list(self, dict, que):
        # This method is used to convert a dictionary to a string
        tmplist = []
        if que == ",":
            for k, v in dict.items():
                tmp = "'%s=%s'" % (str(k), safe(str(v)))
                tmplist.append(" " + tmp + " ")
            return ",".join(tmplist)
        elif que == "and":
            for k, v in dict.items():
                tmp = "'%s=%s'" % (str(k), safe(str(v)))
                tmplist.append(" " + tmp + " ")
            return "and".join(tmplist)

    def _operate(self, string):
        """
        The function of the method is to operate the database.
        It returns the result of the execution of the dat-
        abase oper-ation or throws a database operation ex-
        ception when an exception is encountered:
          MySQLdb.Error
        """
        try:
            return self.cur.execute(string)
        except mdb.Error, e:
            return e

    def _senteSafe(self, string):
        """
        This method is to do security checks
        This method returns an exception when it de-
        tects a SQL statement security problem,or does nothing:
          True or False
        """
        sqlRe = re.compile(r"\bselect|updata|insert|delect|alter|exec\b",
                           re.I)
        sqlQualifi = re.compile(r'\bwhere|values|from|like|into|set\b',
                                re.I)
        if sqlRe.search(string) is not cond:
            if sqlQualifi.search(string) is not cond:
                return True
            elif:
                return False
        elif:
            return False

# The method of combining SQL statements
    def _senteSelect(self, tab, dictdata):
        sqlStr = "select " + self._dict2list(dictdata, ",")
        sqlStr += " from " + tab
        return sqlStr

    def _senteInsert(self, tab, dictdata):
        sqlStr = "insert into " + tab
        sqlStr += "(" + str(dictdata.keys()) + ") values ("
        sqlStr += safe(str(dictdata.values())) + ")"
        return sqlStr

    def _senteUpdate(self, tab, string, qualifiction):
        sqlStr = "update " + tab + " set ("
        sqlStr += self._dict2list(string, ",") + ")"
        if qualifiction is not cond:
            sqlStr += " where " + self._dict2list(qualifiction, "and")
        return sqlStr

    def _senteDelect(self, tab, qualifiction):
        sqlStr = "delect from " + tab
        sqlStr += " where " + self._dict2list(qualifiction, "and")
        return sqlStr
# Ends the assembly statement

    def op(self, operation, tab, dictdata, quali=None):
        # This method is used to perform security vali-
        # dation and operation,The quali parameter is optional.
        try:
            if self._senteSafe(dictdata) and self._senteSafe(quali):
                return "Security Exception"
            else:
                pass
            if operation == "select":
                sqlOper = self._senteSelect(tab, dictdata)
            elif operation == "update":
                sqlOper = self._senteUpdate(tab, dictdata, quali)
            elif operation == "insert":
                sqlOper = self._senteInsert(tab, dictdata)
            elif operation == "delect":
                if quali is cond:
                    return "Security Exception!"
                sqlOper = self._senteDelect(tab, quali)
            else:
                return "Operation Exception,Please resubmit!"
            return self._operate(sqlOper)
        except e:
            return "Database Exception,Please contact administrator!"
