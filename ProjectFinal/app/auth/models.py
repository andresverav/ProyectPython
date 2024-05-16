from datetime import datetime
from app import db, bcrypt
from app import login_manager
from flask_login  import UserMixin

class User (UserMixin, db.model):
    _tablename_ ="user"
    id= db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_mail = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    crete_date = db.column(db.datetime, default=datetime.now())

def check_pasaword(self, password):
    return bcrypt.check_password_hash(self.user_password, password)

@classmethod
def create_user(cls, user, mail, password):
    user=cls(user_name=user,
             user_mail=mail,
             user_password= bcrypt.generate_password_hash(password).decode("utf-8")
            )
    db.sesion.add(user)
    db.sesion.commit()
    return user

@login_manager.user_loader
def loader_user(id):
    return User.query.get(int(id))
    

