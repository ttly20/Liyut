import MySQLdb as mdb
import os

station_init = open("install.sql","r")

try:
    ##create database cursor
    con = mdb.connect("localhost","root","..22lxy.")
    cur = con.cursor()
    ##database operate
    for sqlStr in station_init.readlines():
        print sqlStr
        cur.execute(sqlStr)
    print "database done"
except IOError:
    print "Error:Profile not found!"
except mdb.Error,e:
    try:
        sqlError = "Error %d:%s" % (e.args[0],e.args[1])
    except IndexError:
        print "MySQL Error:%s" % str(e)
finally:
    station_init.close()
    con.close()
