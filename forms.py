# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField,StringField,SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email

class LoginForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default=False)
    submit = SubmitField('Login')
    #提交字段实际并不携带数据因此没有必要在表单类中定义。

class SignUpForm(Form):
    user_name = StringField('user name', validators=[
        DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[
        Email(), DataRequired(), Length(max=128)])
    submit = SubmitField('Sign up')

class AboutMeForm(Form):
    describe = StringField('about me', validators=[
        DataRequired(), Length(max=140)])
    submit = SubmitField('YES!')

class PublishBlogForm(Form):
    pass
