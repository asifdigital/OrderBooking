from flask import Flask, render_template
from flask_session import Session

from models import *

app = Flask(__name__)

DATABASE_URL="postgres://developer:test123@localhost/OrderBooking"
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Session(app)
db.init_app(app)


@app.route('/')
def index():
    bases=UkItem.query.filter_by(type_id=1).all()
    proteins=UkItem.query.filter_by(type_id=2).all()
    sides=UkItem.query.filter_by(type_id=3).all()
    desserts=UkItem.query.filter_by(type_id=4).all()
    return render_template("index.html", bases=bases, proteins=proteins, sides=sides, desserts=desserts)

if __name__ == '__main__':
    app.run()
