from flask_restful import Resource, Api, reqparse, marshal_with, fields
from flask_security import auth_required, roles_required, current_user  
from .model import *

api=Api(prefix='/api')

parser= reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the category is required and should be string')

section_fields={
    "id": fields.Integer,
    "name": fields.String
}


class Api_Section(Resource):
    @marshal_with(section_fields)
    @auth_required("token")
    def get(self):
        all_sections = Section.query.all()
        return all_sections
    
    @auth_required("token")
    @roles_required("customer")
    def post(self):
        args = parser.parse_args()
        section=Section(name=args.get("name"), creator_id=current_user.id)
        db.session.add(section)
        db.session.commit()
        return {"message": "Category created successfully"}

api.add_resource(Api_Section,'/section')