from flask import Blueprint, render_template, request, flash

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
        email = request.form.get('email')
        name = request.form.get('firstName')
        password = request.form.get('password1')
        phonenumber = request.form.get('phoneno')

        if len(email)< 5 or len(name)<3 or len(password) < 3 or len(phonenumber) != 10:
            flash('Make sure your details are correct: Email should be more than 4 charachters, Name and password should be more than three characters and phone number should be ten digits',category='error')
            pass
        else:
            #datbase ko add keejiya bhaiya
            flash("account successful",category='success')
            pass

    return render_template('signup.html')