from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Aircraft, Flight, Order, OrderDetail
from forms import CheckoutForm  # Only import the main form

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flightworld.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'iceman-topgun-secret'

db.init_app(app)

# Inject aircraft list into all templates
@app.context_processor
def inject_aircraft_list():
    return dict(aircraft_list=Aircraft.query.order_by(Aircraft.name).all())

# Home Page
@app.route('/')
def home():
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)

# Aircraft Detail Page
@app.route('/aircraft/<slug>')
def aircraft_detail(slug):
    aircraft = Aircraft.query.filter_by(slug=slug).first_or_404()
    return render_template('aircraft_detail.html', aircraft=aircraft)

# Flight Detail Page
@app.route('/flight/<slug>')
def flight_detail(slug):
    flight = Flight.query.filter_by(slug=slug).first_or_404()
    return render_template('flight_detail.html', flight=flight)

# Flights Listing Page (with optional sorting)
@app.route('/flights')
def flights():
    sort_by = request.args.get('sort_by')
    if sort_by == 'price_asc':
        all_flights = Flight.query.order_by(Flight.price.asc()).all()
    elif sort_by == 'price_desc':
        all_flights = Flight.query.order_by(Flight.price.desc()).all()
    else:
        all_flights = Flight.query.order_by(Flight.name.asc()).all()
    return render_template('flights.html', flights=all_flights)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    flights = Flight.query.filter(Flight.slug.in_(cart)).all() if cart else []
    return render_template('cart.html', flights=flights)

@app.route('/add_to_cart/<slug>')
def add_to_cart(slug):
    cart = session.get('cart', [])
    if slug not in cart:
        cart.append(slug)
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<slug>')
def remove_from_cart(slug):
    cart = session.get('cart', [])
    if slug in cart:
        cart.remove(slug)
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

# Checkout Route
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = session.get('cart', [])
    flights = Flight.query.filter(Flight.slug.in_(cart)).all() if cart else []

    form = CheckoutForm()

    # Ensure the form has the right number of subforms
    while len(form.flights.entries) < len(flights):
        form.flights.append_entry()

    # Populate choices per flight
    for i, flight in enumerate(flights):
        aircraft_choices = [(a.strip(), a.strip()) for a in flight.available_aircraft.split(',')] if flight.available_aircraft else []
        time_choices = [(t.strip(), t.strip()) for t in flight.availability.split(',')] if flight.availability else []

        form.flights[i].aircraft_choice.choices = aircraft_choices
        form.flights[i].time_slot.choices = time_choices

    # Handle form submission
    if form.validate_on_submit():
        new_order = Order(
            customer_name=form.customer_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            total=sum(f.price for f in flights)
        )
        db.session.add(new_order)
        db.session.commit()

        for i, flight in enumerate(flights):
            selected_aircraft = form.flights[i].aircraft_choice.data
            selected_time = form.flights[i].time_slot.data

            detail = OrderDetail(
                order_id=new_order.id,
                product_id=flight.id,
                quantity=1,
                selected_aircraft=selected_aircraft,
                selected_availability=selected_time
            )
            db.session.add(detail)

        db.session.commit()
        session.pop('cart', None)
        flash("✈️ Order confirmed! Welcome to the Danger Zone, ICEMAN.", "success")
        return redirect(url_for('checkout'))

    if form.errors:
        print("❌ Form validation errors:")
        print(form.errors)

    return render_template('checkout.html', form=form, flights=flights)

if __name__ == '__main__':
    app.run(debug=True)
