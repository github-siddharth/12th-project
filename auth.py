from flask import Blueprint, render_template, request, flash
from . import super
auth = Blueprint('auth',__name__)
@auth.route('/login', methods=['GET','POST'] )
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        phonenumber = request.form.get('phoneno')
    a = request.form
    print(a)
       
    return render_template('login.html')
@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        
        global email
        global name
        global password
        global phonenumber
        email = request.form.get('email')
        name = request.form.get('firstName')
        password = request.form.get('password1')
        phonenumber = request.form.get('phoneno')
        print(email,name,password,phonenumber)
        print('hello')
        if len(email)< 5 or len(name)<3 or len(password) < 3 or len(phonenumber) != 10:
            flash('Make sure your details are correct: Email should be more than 4 charachters, Name and password should be more than three characters and phone number should be ten digits',category='error')
            pass
        else:
            #datbase ko add keejiya bhaiya
            flash("account successful",category='success')
            pass
    """ import mysql.connector as mc
    mydb = mc.connect(host = "127.0.0.1",port="5000",user ='root',password = 'sid7superstar')
    mycursor = mydb.cursor()
    mycursor.execute("create database if not exists vault")
    mycursor.execute("use vault")
    mycursor.execute("create table if not exists vaultdetails(id int NOT_NULL AUTO_INCREMENT primary key, email varchar(50),name varchar(50),password int,phoneno int)")
    mycursor.commit()
    def add():
        q = "insert into vaultdetails (email,name,password,phoneno) values({}','{}',{},{})".format(email,name,password,phonenumber)
        mycursor.execute(q)
        mycursor.commit()
    add() """
    super.hello()
    return render_template('signup.html')