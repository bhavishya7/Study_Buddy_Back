from flask import Blueprint, jsonify, request
from models.User import UserSchema, User
from database.database import db
from sqlalchemy import exc

user_bp = Blueprint("user_bp", __name__, url_prefix="/user")


@user_bp.route("/getUserInfo/<id>")
def get_user_info(id):
    user = User.query.filter_by(id=id).first()
    user_schema = UserSchema()
    output = user_schema.dump(user)
    print(output)

    return jsonify(output)
