from flask import Flask, jsonify, request, Response
from database import db
from routes.user import user_routes

app = Flask(__name__)

# database
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://v02uazsj0uc9txhv16fu:pscale_pw_3787lvNnmOePNpDb0OH3qJXV1u96Ysrn35uugaVBcxN@aws.connect.psdb.cloud/scd_tool?ssl={'rejectUnauthorized':true}&ssl_ca=cacert.pem"
db.init_app(app)
with app.app_context():
    db.create_all()

# routes
app.register_blueprint(user_routes)

@app.route("/center", methods=['GET'])
def index():
    center_data = [{
        "id:": 1,
        "name": "Center for Discovery",
        "address": "1234 Main St",
    },
    {
        "id:": 2,
        "name": "The Meadows Ranch",
        "address": "3456 Elm St",
    }]
    return jsonify(center_data)


if __name__ == "__main__":
    app.run(debug=True)