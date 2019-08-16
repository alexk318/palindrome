from __init__ import db
from flask_security import UserMixin, RoleMixin

role_user_link = db.Table('role_user',
                          db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                          db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                          )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)

    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    scores = db.Column(db.Integer(), default=0)

    active = db.Column(db.Boolean(), default=True)

    roles = db.relationship('Role', secondary=role_user_link, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return 'ID: {}, Email: {}'.format(self.id, self.email)



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)

