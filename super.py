from . import auth
def hello():

    import mysql.connector as mc
    mydb = mc.connect(host = "127.0.0.1",port="5000",user ='root',password = 'sid7superstar')
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists vault")
    mycursor.execute("use vault")
    mycursor.execute("create table if not exists vaultdetails(id int NOT_NULL AUTO_INCREMENT primary key, email varchar(50),name varchar(50),password int,phoneno int)")
    mycursor.commit()
    def add():
        q = "insert into vaultdetails (email,name,password,phoneno) values({}','{}',{},{})".format(auth.email,auth.name,auth.password,auth.phonenumber)
        mycursor.execute(q)
        mycursor.commit()
    add()