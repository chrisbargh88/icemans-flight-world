from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Association table: many-to-many between flights and aircraft
flight_aircraft = db.Table(
    'flight_aircraft',
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id'), primary_key=True),
    db.Column('aircraft_id', db.Integer, db.ForeignKey('aircraft.id'), primary_key=True)
)

class Aircraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)  # To link via Excel
    type = db.Column(db.String(100))
    image = db.Column(db.String(100))
    description = db.Column(db.Text)

    # Related flights
    flights = db.relationship('Flight', secondary=flight_aircraft, back_populates='aircraft')


class Flight(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    tagline = db.Column(db.String(100))
    price = db.Column(db.Float)
    image = db.Column(db.String(100))
    short_description = db.Column(db.Text)
    long_description = db.Column(db.Text)
    available_aircraft = db.Column(db.Text)
    availability = db.Column(db.String(200))

    # Related aircraft
    aircraft = db.relationship('Aircraft', secondary=flight_aircraft, back_populates='flights')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(20))
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    order_details = db.relationship('OrderDetail', backref='order', lazy=True)


class OrderDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('flight.id'))
    quantity = db.Column(db.Integer)
    selected_aircraft = db.Column(db.String(100))
    selected_availability = db.Column(db.String(100))