from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from .forms import RegistrationForm, LoginForm
from . import auth
from ..import db
from ..models import User
from ..email import mail_message


@auth.route('templates/auth/reqister',methods=['GET','POST'])
def register():
    """
    Function that registers the users
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    title = "Registration"

    return render_template('auth/register.html', registration_form = form, title = title)

@auth.route('/login',methods=['GET','POST'])
def login():
    """
    Function that checks if the form is validated
    """
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('Invalid Username or Password')

    title = "Blog Post|Login"
    return render_template('auth/login.html', login_form = login_form, title = title)
# @auth.route('/register',methods = ["GET","POST"])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data,password = form.password.data)
#         db.session.add(user)
#         db.session.commit()

#         mail_message("Welcome to Blog Post","email/welcome_user",user.email,user=user)

#         return redirect(url_for('auth.login'))
#         title = "New Account"
#     return render_template('auth/register.html',registration_form = form)

#logout function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))# redirects user to the main page of the app after successful logout
