from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Email

# Subform for individual flight selections
class FlightChoiceForm(FlaskForm):
    class Meta:
        csrf = False  # Disable CSRF for nested subforms

    aircraft_choice = SelectField(
        "Select Aircraft",
        choices=[],  # Populated dynamically in app.py
        validators=[DataRequired()]
    )
    
    time_slot = SelectField(
        "Select Time Slot",
        choices=[],  # Populated dynamically in app.py
        validators=[DataRequired()]
    )

# Main checkout form
class CheckoutForm(FlaskForm):
    customer_name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )
    
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    phone_number = StringField(
        "Phone Number",
        validators=[DataRequired()]
    )

    flights = FieldList(
        FormField(FlightChoiceForm),
        min_entries=0  # Will be added dynamically in app.py
    )

    submit = SubmitField("Place Order")