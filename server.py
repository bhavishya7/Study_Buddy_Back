from flask import Flask
from database.database import db, ma, mi
from models.User import UserSchema, User


def create_app():
    app = Flask(__name__)
    database_string = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
        "postgres",
        "postgres",
        "localhost",
        "5432",
        "postgres",)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    mi.init_app(app, db)
    return app


def setup_routes(app):
    from auth.routes import auth_bp
    from user.routes import user_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)


app = create_app()

setup_routes(app)


@app.route("/")
def index():
    return "Hello world!!"


@app.route("/test", methods=["POST", "GET"])
def test():
    return "TEST"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

# if __name__ == "__main__":
#   app.run(debug=True)
