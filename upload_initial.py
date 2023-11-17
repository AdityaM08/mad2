from main import app
# from application.sec import datastore
from applications.model import db, Role
from flask_security import hash_password
from werkzeug.security import generate_password_hash
from applications.sec import *

with app.app_context():
    db.create_all()
    # admin = Role(id="admin", name="admin", description="User is an admin")
    # db.session.add(admin)
    # manager = Role(id="manager", name="manager", description="User is a manager")
    # db.session.add(manager)
    # user = Role(id="user", name="user", description="User is a user")
    # db.session.add(user)
    datastore.find_or_create_role(name="admin", description="User is an admin")
    datastore.find_or_create_role(name="manager", description="User is a manager")
    datastore.find_or_create_role(name="customer", description="User is a customer")
    db.session.commit()
    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(email="admin@email.com", password=generate_password_hash("admin"), roles=["admin"])
    if not datastore.find_user(email="manager1@email.com"):
        datastore.create_user(email="manager1@email.com", password=generate_password_hash("manager1"), roles=["manager"], active=False)   
    if not datastore.find_user(email="customer1@email.com"):
        datastore.create_user(email="customer1@email.com", password=generate_password_hash("customer1"), roles=["customer"])
    # try:
    db.session.commit()
    # except:
    #     pass