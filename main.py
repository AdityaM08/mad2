from flask import Flask
from applications.model import *
from config import *
from applications.resources import *
from flask_security import SQLAlchemyUserDatastore, Security
from applications.sec import *

def make_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///grocery.sqlite3"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SECRET_KEY'] = 'malikaditya'
    db.init_app(app)
    api.init_app(app)
    
    app.security = Security(app, datastore)
    with app.app_context():
        import applications.views
    return app


app = make_app()

# from applications.user import *
# from applications.admin import *


if __name__ == "__main__":
    # db.create_all()
    # admin = User.query.filter_by(is_admin = True).first()
    # if not admin:
    #     admin_new = User(name = "Manager", email = "admin@grocery.com", 
    #                      password = "0000", is_admin = True)
    #     db.session.add(admin_new)
    #     db.session.commit()
    app.run(debug = True)