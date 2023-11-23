from flask_restful import Resource, Api, reqparse, fields, marshal
from flask_security import auth_required, roles_required, current_user  
from .model import *
from flask import jsonify
from sqlalchemy import or_

api=Api(prefix='/api')

parser= reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the category is required and should be string')

class Creator(fields.Raw):
    def format(self, user):
        return user.email


section_fields={
    "id": fields.Integer,
    "name": fields.String,
    'is_approved': fields.Boolean,
    'creator': Creator
}


class Api_Section(Resource):
    @auth_required("token")
    def get(self):
        if "admin" in current_user.roles:
            sections = Section.query.all()
        else:
            sections = Section.query.filter(
                or_(Section.is_approved == True, Section.creator == current_user)).all()
        if len(sections) > 0:
            return marshal(sections, section_fields)
        else:
            return {"message": "No Resourse Found"}, 404

    
    @auth_required("token")
    @roles_required("manager")
    def post(self):
        args = parser.parse_args()
        section=Section(name=args.get("name"), creator_id=current_user.id)
        db.session.add(section)
        db.session.commit()
        return {"message": "Category created successfully"}

api.add_resource(Api_Section,'/section')