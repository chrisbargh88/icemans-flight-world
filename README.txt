.___                                    
|   | ____  ____   _____ _____    ____  
|   |/ ___\/ __ \ /     \\__  \  /    \ 
|   \\  \__\  ___/|  Y Y  \/ __ \|   |  \
|___|\___  >___  >__|_|  |____  /___|  /
         \/    \/      \/     \/     \/

ICEMAN’s FLIGHT WORLD

Retro 1980s-themed ecommerce web application to book flight 
experiences like aerobatic rides or training in jets. 

============================
Technologies Used
============================
- HTML / CSS
- Bootstrap via CDN
- Python 3.7+
- Flask Templates
- Flask-WTForms
- Flask SQLAlchemy

============================
Launch Checklist
============================

1. Prerequisites
• Python 3.7+ installed
• Visual Studio Code (recommended)
• Open folder `startwebapphere` in VS Code

2. Install Dependencies (run in terminal)

```
pip install flask_sqlalchemy
pip install flask-wtf
pip install email-validator
```

3. Run the App

```
python app.py
```

============================
Database Management
============================

To reseed database:

```
python full_seed_db.py
```

To reinitialize database:

Create `init_db.py` with:

```python
from app import app, db

with app.app_context():
    db.create_all()
    print(" Database tables created successfully.")
```

Then run:

```
python init_db.py
```

To fully wipe and rebuild (sometimes youll need to run lines 2-5 all at once not individually):

```
python
>>> python
>>> from app import app, db
>>> with app.app_context():
>>> db.drop_all()
>>> db.create_all()
>>> exit()
```

============================
Troubleshooting
============================

Windows App Execution Aliases

Turn off:
• `python.exe`
• `python3.exe`

Go to: **Settings > Apps > App Execution Aliases**

============================
Data Model Notes
============================

• A **many-to-many** relationship exists between `Flights` and `Aircraft`, as a flight experience may be available 
across multiple aircraft, and each aircraft may support multiple flight types.

• Implemented in SQLAlchemy using a secondary association table.

• Additionally, there is a **one-to-many** relationship from `Aircraft` to `Flights` when displaying grouped 
flight experiences for a selected aircraft (e.g. F-14B [Danger Close, Rough Strip Rumble, etc.]).

These relationships support dynamic browsing and booking flexibility.

========================================
Viewing Orders in DB Browser for SQLite
========================================

To inspect or verify order data manually:

1. Open the `flightworld.db` file in **DB Browser for SQLite**.
2. Navigate to the `Browse Data` tab.
3. Select the `Orders` or `Order_Details` table from the dropdown.
4. Review customer submissions, selected flights, and timestamps.

Use this SQL command to view the flight time selected and aircraft selected:

SELECT
    o.id AS order_id,
    o.customer_name,
    o.email,
    o.phone_number,
    f.name AS flight_name,
    f.price,
    od.quantity,
    od.selected_aircraft,
    od.selected_availability,
    o.created_at
FROM order_detail od
JOIN "order" o ON od.order_id = o.id
JOIN flight f ON od.product_id = f.id
ORDER BY o.id DESC;


### Additional Troubleshooting & Developer Tips

#### CSRF Token Errors (Forms Not Submitting)
If WTForms throw CSRF errors:
- Ensure `SECRET_KEY` is set in `app.config`
- Do not forget `{{ form.hidden_tag() }}` in the form template
- Restart the dev server after modifying form structure

#### Stale or Broken Database (Orders not saving)
If orders are not appearing in DB Browser:
- Stop the server and **delete `flightworld.db` manually**
- Rebuild using `init_db.py` and `full_seed_db.py`
- Then relaunch with: `python app.py`

#### Form Validation Silent Failures
If you hit submit and nothing happens:
- Check for silent form errors in the terminal (these are printed on submit)
- Make sure dropdowns like `aircraft_choice` and `time_slot` are being dynamically populated in `app.py` before `form.validate_on_submit()` is called

#### Python Package Issues
If `flask`, `flask_sqlalchemy`, or `flask_wtf` throw `ModuleNotFoundError`:
- Run:  
  ```
  pip install -r requirements.txt
  ```
- Or re-install manually:
  ```
  pip install flask flask_sqlalchemy flask_wtf email-validator
  ```

#### Prevent Double Orders (Optional Future Tip)
To prevent users from refreshing `/checkout` and submitting twice:
- After a successful order, redirect to a `/success` route
- Or implement `POST-Redirect-GET` more explicitly

============================
Author
============================

Christopher Ian Bargh
Callsign: "Jagg3d"
christopherbargh@gmail.com
https://www.linkedin.com/in/chris-bargh/