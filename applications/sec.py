from flask_security import SQLAlchemyUserDatastore
from .model import *
datastore = SQLAlchemyUserDatastore(db,User, Role)