# -*- coding:utf-8 -*-
from flask import render_template,request,g,url_for
from app import app, lm
from database import Session
from models import User

import datetime
from flask_login import login_user, logout_user, current_user,login_required
import datetime

import pdb

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # 用户名
    posts = [  # 提交内容
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


from flask import render_template, flash, redirect
from forms import LoginForm

# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for Name: ' + form.name.data)
#         flash('passwd: ' + str(form.password.data))
#         flash('remember_me: ' + str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html',
#                            title = 'Sign In',
#                            form = form)

@lm.user_loader
def load_user(user_id):
    session = Session()
    r = session.query(User).get(int(user_id))
    session.commit()
    return r

@app.route('/login',methods = ['GET','POST'])
def login():
    # 验证用户是否被验证
    # if current_user.is_authenticated:
    #     flash('current user:'+current_user.nickname)
    #     return redirect('index')

    # 注册验证
    form = LoginForm()
    if form.validate_on_submit():
        print("**************")
        print(request.form.get('user_name'))
        print("**************")
        user = User.login_check(request.form.get('user_name'))
        print user
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("index", user_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')

    return render_template(
        "login.html",
        title="Sign In",
        form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

from forms import LoginForm,SignUpForm

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        register_check = User.login_check(user_name)
        if register_check:
            flash("error: The user's name already exists!")
            return redirect('/sign-up')

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email

            try:
                session = Session()
                session.add(user)
                session.commit()
            except:
                flash("The Database error!")
                return redirect('/sign-up')

            flash("Sign up successful!")
            return redirect('/index')

    return render_template(
        "sign_up.html",
        form=form)


from forms import LoginForm,  SignUpForm, AboutMeForm,PublishBlogForm


@app.route('/user/<int:user_id>', methods=["POST", "GET"])
@login_required#not friendly
def users(user_id):
    form = AboutMeForm()
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        flash("The user is not exist.")
        redirect("/index")

    blogs = user.posts

    return render_template(
        "user2.html",
        form=form,
        user=user,
        blogs=blogs)


@app.route('/publish/<int:user_id>', methods=["POST", "GET"])
@login_required
def publish(user_id):
    pass

@app.route('/about_me/<int:user_id>')
def aboutme(user_id):
    pass