from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired,Length

class UsermodifyForm(FlaskForm):
    userPasswd = PasswordField('비밀번호', validators=[DataRequired()])
    userName = StringField('이름', validators=[DataRequired()])
    userSex = StringField('성별', validators=[DataRequired()])

class SignupForm(FlaskForm):
    userID = StringField('아이디', validators=[DataRequired()])
    userPasswd = PasswordField('비밀번호', validators=[DataRequired()])
    userName = StringField('이름', validators=[DataRequired()])
    userSex = StringField('성별', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    userID = StringField('아이디', validators=[DataRequired(), Length(min=3, max=25)])
    userPasswd = PasswordField('비밀번호', validators=[DataRequired()])

class RegistForm(FlaskForm):
    lec_name = StringField('강의명', validators=[DataRequired()])
    pro_name = StringField('교수명', validators=[DataRequired()])
    lec_skill = StringField('강의력', validators=[DataRequired()])
    lec_level = StringField('난이도', validators=[DataRequired()])
    content_title = StringField('제목', validators=[DataRequired()])
    eval_contents = StringField('내용', validators=[DataRequired()])

