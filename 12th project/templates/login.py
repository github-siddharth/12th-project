import mysql.connector

import mysql.connector as mc
mycon=mc.connect(host="localhost",user='root',password='sid7superstar')
cur=mycon.cursor()
cur.execute("create database if not exists sidmad")
cur.execute("use sidmad")
cur.execute("create table if not exists userdet(user_id int NOT NULL AUTO_INCREMENT,name varchar(26),password varchar(30),primary key(user_id))")
def signin(name,pw):
    try:
      q = "insert into userdt values('{}','{}')".format()
    except:
       print("already available..try logging in")
mycon.commit()