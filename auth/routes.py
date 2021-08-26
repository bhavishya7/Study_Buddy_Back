from flask import Blueprint, jsonify, request
from models.User import UserSchema, User
from database.database import db
from sqlalchemy import exc

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


@auth_bp.route("/")
def auth_index():
    new_user = User(email="abc@gmail.com", first_name="ABC", last_name="DEF")
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.id)


@auth_bp.route("/getUser")
def get_user():
    user = User().query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(user)

    return jsonify(output)


@auth_bp.route("/addUser", methods=["POST", "GET"])
def add_user():
    request_data = request.get_json(force=True)
    print(request_data)
    print("Add users")
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    email = request_data['email']
    pronouns = request_data['pronouns']
    major = request_data['major']
    grad_year = request_data['grad_year']
    current_classes = request_data['current_classes']
    pref_time = request_data['pref_time']
    study_locations = request_data['study_locations']
    new_user = User(email=email, first_name=first_name, last_name=last_name, pronouns=pronouns, major=major,
                    grad_year=grad_year, current_classes=current_classes, pref_time=pref_time,
                    study_locations=study_locations)
    try:
        db.session.add(new_user)
        db.session.commit()
    except exc.SQLAlchemyError as e:
        return jsonify({"status": "BAD", "msg": str(e)}), 401

    user_output = {
        "id": new_user.id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "email": new_user.email,
        "pronouns": new_user.pronouns,
        "major": new_user.major,
        "grad_year": new_user.grad_year,
        "current_classes": new_user.current_classes,
        "pref_time": new_user.pref_time,
        "study_locations": new_user.study_locations,
    }
    return jsonify(user_output), 200
