from app import db

class User(db.Model):
        __tablename__ = "user"
        userID=db.Column(db.String(20),primary_key=True)
        userPasswd=db.Column(db.String(150),nullable=False)
        userName=db.Column(db.String(20),nullable=False)
        userSex=db.Column(db.String(20),nullable=False)

class Evaluate(db.Model):
        __tablename__ = "evaluate"
        evalID=db.Column(db.Integer,primary_key=True)
        writer=db.Column(db.String(20),nullable=False)
        lec_name=db.Column(db.String(20),nullable=False)
        pro_name=db.Column(db.String(20),nullable=False)
        content_title=db.Column(db.String(50),nullable=False)
        lec_skill=db.Column(db.String(20),nullable=False)
        lec_level=db.Column(db.String(20),nullable=False)
        eval_contents=db.Column(db.String(20),nullable=False)
