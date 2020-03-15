# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship, sessionmaker
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True,server_default=db.FetchedValue())
    session_id = db.Column(db.String(256), nullable=False)
    base_id = db.Column(db.Integer, nullable=False)
    base_name = db.Column(db.String(50), nullable=False)
    protein_id = db.Column(db.Integer, nullable=False)
    protein_name = db.Column(db.String(50), nullable=False)
    side1_id = db.Column(db.Integer, nullable=False)
    side1_name = db.Column(db.String(50), nullable=False)
    side2_id = db.Column(db.Integer, nullable=False)
    side2_name = db.Column(db.String(50), nullable=False)
    dessert_id = db.Column(db.Integer, nullable=False)
    dessert_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class ItemType(db.Model):
    __tablename__ = 'item_type'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type = db.Column(db.String(25), nullable=False)



class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type_id = db.Column(db.ForeignKey('item_type.id'), nullable=False)
    item_name = db.Column(db.String(50), nullable=False)
    item_description = db.Column(db.String(50), nullable=False)

    type = db.relationship('ItemType', primaryjoin='Item.type_id == ItemType.id', backref='items')



class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_id = db.Column(db.ForeignKey('orders.id'), nullable=False)
    box_id = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.ForeignKey('items.id'), nullable=False)

    item = db.relationship('Item', primaryjoin='OrderDetail.item_id == Item.id', backref='order_details')
    order = db.relationship('Order', primaryjoin='OrderDetail.order_id == Order.id', backref='order_details')



class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_date = db.Column(db.DateTime, server_default=db.FetchedValue())
    delivery_date = db.Column(db.Date, nullable=False)
    order_amount = db.Column(db.Numeric, nullable=False)
    promo_code = db.Column(db.String(12))
    discount_amount = db.Column(db.Numeric, nullable=False)
    tax_amount = db.Column(db.Numeric, nullable=False)
    delivery_method = db.Column(db.Integer, nullable=False)
    delivery_amount = db.Column(db.Numeric, nullable=False)
    total_amount = db.Column(db.Numeric, nullable=False)
    payment_method = db.Column(db.Integer, nullable=False)
    payment_status = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text)



class UkDeliveryAddres(db.Model):
    __tablename__ = 'uk_delivery_address'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_id = db.Column(db.ForeignKey('orders.id'), nullable=False)
    mobile_number = db.Column(db.String(25), nullable=False)
    address1 = db.Column(db.String(256), nullable=False)
    address2 = db.Column(db.String(256))
    city = db.Column(db.String(25), nullable=False)
    town = db.Column(db.String(25), nullable=False)
    post_code = db.Column(db.String(8), nullable=False)

    order = db.relationship('Order', primaryjoin='UkDeliveryAddres.order_id == Order.id', backref='uk_delivery_address')



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    username = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256), nullable=False)
    hint = db.Column(db.String(25), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())

class Price(db.Model):
    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type = db.Column(db.String(25), nullable=False)
    amount = db.Column(db.DECIMAL, nullable=False)
