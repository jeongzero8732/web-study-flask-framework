from flask import Blueprint,render_template,url_for, flash, request,session,g
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import redirect
import functools
from app import db
from ..forms import SignupForm, UserLoginForm, UsermodifyForm,RegistForm
from ..models import User,Evaluate
import logging

bp = Blueprint('evaluate', __name__, url_prefix='/evaluate')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user = session.get('user')
    if user is None:
        g.user = None
    else:
        g.user = User.query.get(user)


@bp.route('/')
def evaluate():
    page = request.args.get('page', type=int, default=1)
    list_ = Evaluate.query.order_by(Evaluate.evalID.desc())
    list_ = list_.paginate(page, per_page=5)
    return render_template('evaluate/evaluation.html',list_=list_)

@bp.route('/list/')
def _list():
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    
     # 조회
    question_list = Evaluate.query.order_by(Evaluate.evalID.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        question_list = question_list.filter(Evaluate.content_title.ilike(search) |  # 제목
                    Evaluate.eval_contents.ilike(search) |  # 내용
                    Evaluate.writer.ilike(search) |  # 작성자
                    Evaluate.lec_name.ilike(search) |  # 강의명
                    Evaluate.pro_name.ilike(search)  # 교수명
                    ) \
            .distinct()

    # 페이징
    question_list = question_list.paginate(page, per_page=5)
    return render_template('evaluate/evaluation.html', list_=question_list, page=page, kw=kw)

@bp.route('/update/<int:evaluate_id>/',methods=('GET','POST'))
def update(evaluate_id):
    form=RegistForm()
    e = Evaluate.query.get(evaluate_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            e.lec_name=form.lec_name.data
            e.pro_name=form.pro_name.data
            e.lec_skill=form.lec_skill.data
            e.lec_level=form.lec_level.data
            e.content_title=form.content_title.data
            e.eval_contents=form.eval_contents.data
            db.session.commit()
            flash('수정 완료!!!!')
            return redirect(url_for('evaluate.evaluate'))
    return render_template('evaluate/evaluate_update.html', form=form,evaluate_=e)

@bp.route('/detail/<int:evaluate_id>/',methods=('GET','POST'))
def detail(evaluate_id):
    evaluate_ = Evaluate.query.get(evaluate_id)
    return render_template('evaluate/evaulate_detail.html', evaluate_=evaluate_)

@bp.route('/delete/<int:evaluate_id>')
@login_required
def delete(evaluate_id):
    e = Evaluate.query.get_or_404(evaluate_id)
    if g.user.userID != e.writer:
        flash('삭제권한이 없습니다')
        return redirect(url_for('evaluate.evaluate',evaluate_=e))
    db.session.delete(e)
    db.session.commit()
    return redirect(url_for('evaluate.evaluate'))

@bp.route('/register',methods=('GET','POST'))
@login_required
def register():
    form=RegistForm()
    if request.method == 'POST':
        # return 'aaa'
        if form.validate_on_submit(): 
            e = Evaluate(lec_name=form.lec_name.data,
            pro_name=form.pro_name.data,
            lec_skill=form.lec_skill.data,
            lec_level=form.lec_level.data,
            content_title=form.content_title.data,
            eval_contents=form.eval_contents.data,
            writer=g.user.userID)
            db.session.add(e)
            db.session.commit()
            flash('등록 성공!!')
            return redirect(url_for('evaluate.evaluate'))
    return render_template('evaluate/evaluation_insert.html',form=form)