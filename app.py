from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from sqlalchemy.exc import SQLAlchemyError

from models import *

app = Flask(__name__)

DATABASE_URL = "postgres://developer:test123@localhost/OrderBooking"
# if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "adsfkjdasdasdfasdf"
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Session(app)
db.init_app(app)


@app.before_first_request
def once_only():
    session['sid'] = session.sid


@app.route('/')
def index():
    sid = session['sid']

    bases = Item.query \
        .join(ItemType, Item.type_id == ItemType.id) \
        .add_columns(Item.id, Item.item_name, Item.item_description) \
        .filter(Item.type_id == ItemType.id) \
        .filter(ItemType.type == "Base")

    proteins = Item.query \
        .join(ItemType, Item.type_id == ItemType.id) \
        .add_columns(Item.id, Item.item_name, Item.item_description) \
        .filter(Item.type_id == ItemType.id) \
        .filter(ItemType.type == "Protein")

    sides = Item.query \
        .join(ItemType, Item.type_id == ItemType.id) \
        .add_columns(Item.id, Item.item_name, Item.item_description) \
        .filter(Item.type_id == ItemType.id) \
        .filter(ItemType.type == "Side")

    desserts = Item.query \
        .join(ItemType, Item.type_id == ItemType.id) \
        .add_columns(Item.id, Item.item_name, Item.item_description) \
        .filter(Item.type_id == ItemType.id) \
        .filter(ItemType.type == "Dessert")

    price = Price.query.filter(Price.type == "Standard Meal").first()

    items = Cart.query.filter(Cart.session_id == sid).all()

    return render_template("index.html", bases=bases, proteins=proteins, sides=sides, desserts=desserts, items=items,
                           sid=sid, price=price)


@app.route('/cart', methods=["POST"])
def cart():
    sid = session['sid']

    base_id = int(request.form.get("base_id"))
    protein_id = int(request.form.get("protein_id"))
    dessert_id = int(request.form.get("dessert_id"))
    sides = request.form.get("side_id")
    side_id = sides.split(",")

    base = Item.query.filter(Item.id == base_id).first()
    protein = Item.query.filter(Item.id == protein_id).first()
    dessert = Item.query.filter(Item.id == dessert_id).first()
    side1 = Item.query.filter(Item.id == side_id[0]).first()
    side2 = Item.query.filter(Item.id == side_id[1]).first()

    price = Price.query.filter(Price.type == 'Standard Meal').first()

    user_cart = Cart(
        session_id=sid,
        base_id=base.id,
        base_name=base.item_name,
        protein_id=protein.id,
        protein_name=protein.item_name,
        side1_id=side1.id,
        side1_name=side1.item_name,
        side2_id=side2.id,
        side2_name=side2.item_name,
        dessert_id=dessert.id,
        dessert_name=dessert.item_name,
        quantity=1
    )

    db.session.add(user_cart)
    db.session.commit()
    cart_info = Cart.query.first()

    data = jsonify({
        "rid": cart_info.id,
        "price": price.amount,
        "base": {
            "name": base.item_name,
        },
        "protein": {
            "name": protein.item_name
        },
        "side": {
            "name1": side1.item_name,
            "name2": side2.item_name
        },
        "dessert": {
            "name": dessert.item_name
        }
    });

    return data


@app.route('/removeCartItem', methods=["POST"])
def remove_cart_item():
    sid = session['sid']
    rid = int(request.form.get("rid"))

    cart_item = Cart.query.filter(Cart.id == rid, Cart.session_id == sid).first()
    db.session.delete(cart_item)
    db.session.commit()


@app.route('/updateCartItem', methods=["POST"])
def update_cart_item():
    sid = session['sid']
    rid = request.form.get("rid")
    quantity = request.form.get("quantity")

    cart_item = Cart.query.filter(Cart.id == int(rid), Cart.session_id == sid).first()
    cart_item.quantity = quantity
    db.session.commit()


if __name__ == '__main__':
    app.run()
