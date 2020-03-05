# coding: utf-8
#from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Text
#from sqlalchemy.schema import FetchedValue
#from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

#flask-sqlacodegen --flask --outfile models.py postgres://developer:test123@localhost/OrderBooking

db = SQLAlchemy()


class UkDeliveryAddres(db.Model):
    __tablename__ = 'uk_delivery_address'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_id = db.Column(db.ForeignKey('uk_orders.id'), nullable=False)
    mobile_number = db.Column(db.String(25), nullable=False)
    address1 = db.Column(db.String(256), nullable=False)
    address2 = db.Column(db.String(256))
    city = db.Column(db.String(25), nullable=False)
    town = db.Column(db.String(25), nullable=False)
    post_code = db.Column(db.String(8), nullable=False)
    lat = db.Column(db.Float(53), nullable=False)
    long = db.Column(db.Float(53), nullable=False)

    order = db.relationship('UkOrder', primaryjoin='UkDeliveryAddres.order_id == UkOrder.id', backref='uk_delivery_address')



class UkItemType(db.Model):
    __tablename__ = 'uk_item_type'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type = db.Column(db.String(25), nullable=False)



class UkItem(db.Model):
    __tablename__ = 'uk_items'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    item_name = db.Column(db.String(50), nullable=False)
    type_id = db.Column(db.ForeignKey('uk_item_type.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)

    type = db.relationship('UkItemType', primaryjoin='UkItem.type_id == UkItemType.id', backref='uk_items')



class UkOrderDetail(db.Model):
    __tablename__ = 'uk_order_detail'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_id = db.Column(db.ForeignKey('uk_orders.id'), nullable=False)
    item_id = db.Column(db.ForeignKey('uk_items.id'), nullable=False)
    unit_price = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Numeric, nullable=False)

    item = db.relationship('UkItem', primaryjoin='UkOrderDetail.item_id == UkItem.id', backref='uk_order_details')
    order = db.relationship('UkOrder', primaryjoin='UkOrderDetail.order_id == UkOrder.id', backref='uk_order_details')



class UkOrder(db.Model):
    __tablename__ = 'uk_orders'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    order_date = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    delivery_date = db.Column(db.Date, nullable=False)
    invoice_number = db.Column(db.String(25), nullable=False)
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



class UkProfile(db.Model):
    __tablename__ = 'uk_profile'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(256), nullable=False)
    last_name = db.Column(db.String(256), nullable=False)
    mobile_number = db.Column(db.String(25), nullable=False)
    address1 = db.Column(db.String(256), nullable=False)
    address2 = db.Column(db.String(256))
    city = db.Column(db.String(25), nullable=False)
    town = db.Column(db.String(25), nullable=False)
    post_code = db.Column(db.String(8), nullable=False)
    lat = db.Column(db.Float(53), nullable=False)
    long = db.Column(db.Float(53), nullable=False)

    user = db.relationship('User', primaryjoin='UkProfile.user_id == User.id', backref='uk_profiles')



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    username = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256), nullable=False)
    hint = db.Column(db.String(25), nullable=False)
    country_code = db.Column(db.String(3), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
