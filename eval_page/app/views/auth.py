from flask import Blueprint,render_template,url_for, flash, request,session,g
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import redirect

from app import db
from ..forms import SignupForm, UserLoginForm, UsermodifyForm
from ..views.evaluate import login_required
from ..models import User
import logging

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.before_app_request
def load_logged_in_user():
    user = session.get('user')
    if user is None:
        g.user = None
    else:
        g.user = User.query.get(user)

@bp.route('/')
def index():
    return render_template('./index.html')

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(userID=form.userID.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.userPasswd, form.userPasswd.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user'] = user.userID
            flash('로그인 성공!!')
            return redirect(url_for('auth.index'))
        flash(error)
    return render_template('page/login.html', form=form)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))

@bp.route('/delete')
@login_required
def delete():
    u = User.query.get_or_404(g.user.userID)
    if g.user == None:
        flash('삭제권한이 없습니다')
        return redirect(url_for('auth.index'))
    db.session.delete(u)
    db.session.commit()
    return redirect(url_for('auth.index'))

@bp.route('/user_update/',methods=('GET','POST'))
@login_required
def user_update():
    form = UsermodifyForm()
    if request.method == 'POST':
            if form.validate_on_submit():
                user = User.query.get(g.user.userID)
                user.userPasswd=generate_password_hash(form.userPasswd.data)
                user.userName=form.userName.data
                user.userSex=form.userSex.data
                db.session.commit()
                flash('회원 정보 수정 완료!!!!')
                return redirect(url_for('auth.index'))
            else:
                flash('수정 에러!')
    return render_template('page/userinfo.html', form=form)

@bp.route('/signup/',methods=('GET','POST'))
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(userID=form.userID.data).first()
        if not user:
            user = User(userID=form.userID.data,
                        userPasswd=generate_password_hash(form.userPasswd.data),
                        userName=form.userName.data,
                        userSex=form.userSex.data)
            db.session.add(user)
            db.session.commit()
            flash('회원가입 성공!!')
            return redirect(url_for('auth.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    
    return render_template('page/signup.html',form=form)