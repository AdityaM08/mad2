from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    # role_id = db.Column(db.String, db.ForeignKey('role.id'))
    roles = db.relationship('Role', secondary='roles_users',
                         backref=db.backref('users', lazy='dynamic'))
    section = db.relationship('Section', backref='creator')
    
    # carts = relationship('Cart', backref='user', lazy=True)
    # orders = relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return "<User %r>" % self.name

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Section(db.Model):
    c_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    products = relationship('Product', backref='section',
                            lazy=True, cascade="all, delete-orphan")
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<category {self.name}>"

class Product(db.Model):
    p_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rate = db.Column(db.Integer(), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    sold = db.Column(db.Integer(), nullable=False, default=0)
    unit = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(100))
    category = db.Column(db.String(50), nullable=False)
    c_id = db.Column(db.Integer(), db.ForeignKey('section.c_id'), nullable=False)
    carts = relationship('Cart', backref='product',
                         lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<product {self.name}>"

class Cart(db.Model):
    cart_id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey("product.p_id"), nullable=False)

class Order(db.Model):
    o_id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False)
    total = db.Column(db.Integer(), nullable=False)
    rate = db.Column(db.Integer(), nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)