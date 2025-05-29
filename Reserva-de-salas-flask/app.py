from flask import Flask
from database import db
from reserva_route import routes
from config import config

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
