from app import app, db
from models import Flight, Aircraft

with app.app_context():
    db.drop_all()
    db.create_all()

    aircraft_data = [
        Aircraft(
            name="Mirage F-1",
            slug="mirage_f1",
            type="The Cobra in the Clouds",
            image="mirage_f1.png",
            description="""This French beauty brings Cold War swagger and Mach 2 menace. Sleek, snappy, and sassier than your ex on Red Bull. Perfect for simulated dogfights with plenty of Gallic flair."""
        ),
        Aircraft(
            name="Cessna 182T ",
            slug="cessna_182t",
            type="Dads Reliable Tank",
            image="cessna_182T.png",
            description="""The flying equivalent of a cargo-pants-wearing, lawn-mowing, practical dad. Rugged, trusty, and loves a bit of sightseeing. Also: comes with cup holders (kinda)."""
        ),
        Aircraft(
            name="Boeing Stearman ",
            slug="boeing_stearman",
            type="Barnstormers Dream",
            image="boeing_stearman.png",
            description="""Strap on a scarf and relive the Golden Age of aviation. Open cockpit, canvas wings, and more nostalgia than a VHS copy of Iron Eagle. Flip it, roll it, love it."""
        ),
        Aircraft(
            name="Beechcraft Baron B55 ",
            slug="beechcraft_baron",
            type="Twin-Prop CEO Shuttle",
            image="beechcraft_baron.png",
            description="""Two engines, double the responsibility. Classy, fast, and flies like it knows it owns a yacht. Suitable for business pilots and anyone wearing loafers with no socks."""
        ),
        Aircraft(
            name="F-14B Tomcat ",
            slug="f_14b_tomcat",
            type="The Danger Zone Itself",
            image="f14b_tomcat.png",
            description="""Legend. Icon. Cat with claws. Fire off simulated missiles and sweep those wings like you're in a recruitment ad for 1986. Goose not included.
"""
        ),
        Aircraft(
            name="King Air C90GTi ",
            slug="king_air",
            type="Royalty with Rotors",
            image="king_air.png",
            description="""Luxury in the skies — twin-turboprop elegance meets reliable muscle. Ride smooth, look rich, and maybe even sip a fictional mimosa mid-flight."""
        ),
        Aircraft(
            name="Super Tucano ",
            slug="super_tucano",
            type="Jungle Jet Jockey",
            image="super_tucano.png",
            description="""Brazilian badass with turboprop attitude. Ideal for combat sims, low passes, and waking the cows up near Ray's Airfield. Packs more punch than it should."""
        ),
        Aircraft(
            name="UH-1 Huey ",
            slug="uh_1 huey",
            type="Vietnam Vibes, Berry Edition",
            image="huey.png",
            description="""hat wop-wop-wop sound? That's freedom. Slap on some CCR and take this legend for a tour that feels like a movie montage. Doors optional.
"""
        ),
        Aircraft(
            name="Cirrus SR20 ",
            slug="cirrus_sr20",
            type="Skybound Tech Bro",
            image="cirrus.png",
            description="""Glass cockpit, safety parachute, millennial-friendly. It's like flying an iPhone — sleek, smart, and probably judgmental if you spill coffee.
"""
        ),
        Aircraft(
            name=" Pitts Special S2B ",
            slug="pitts_special",
            type="The Rodeo Clown of the Sky",
            image="pitts_special.png",
            description="""Tiny. Twitchy. Terrifying. Built for advanced aerobatics and certain doom if you sneeze at the wrong time. The thrill-seeker's weapon of choice."""
        ),
        Aircraft(
            name="Piper Warrior PA2",
            slug="piper_warrior",
            type="Mr Reliable",
            image="piper_warrior.png",
            description="""If aircraft had yearbooks, this one would win "Most Approachable." Every pilot's first love. Simple, forgiving, and always down for another lap."""
        ),
        Aircraft(
            name="F-4 Phantom",
            slug="f_4phantom",
            type="Sonic Boom Daddy",
            image="f4_phantom.png",
            description="""She's ugly. She's loud. She's an absolute unit. Once terrified MiGs across Asia — now she terrifies students trying to taxi in a straight line. Retired? Not here."""
        ),
        Aircraft(
            name="L-39C Albatros",
            slug="l_39c_albatros",
            type="Trainer with Teeth",
            image="albatros.png",
            description="""Soviet-bloc chic meets high-performance sass. Jet trainer turned light attack platform. Great for simulated combat flights or if you just want to look intimidating at idle."""
        ),
    ]

    for aircraft in aircraft_data:
        db.session.add(aircraft)
    db.session.flush()

    aircraft_by_slug = {a.slug: a for a in Aircraft.query.all()}

    flights = [
                Flight(
            slug="roll_rumble",
            name="Roll & Rumble",
            tagline="Aerobatic Mayhem",
            price=249,
            image="roll_rumble.png",
            short_description="""Full-throttle aerobatics with rolls, flips, and pure G-force fun""",
            long_description="""Tumble, roll, loop, and spin through the sky in our high-G thrill ride. This is no sightseeing tour — it's a test of guts, grit, and gravity. Bring spare underwear.""",
            available_aircraft="""Boeing Stearman, Super Tucano, 
        Pitts Special S2B""",
            availability="""Monday 4pm, Tuesday 1pm, Friday 11am"""
        ),
        
                Flight(
            slug="rough_strip_rumble",
            name="Rough Strip Rumble",
            tagline="Bush Ops 101",
            price=229,
            image="rough_strip_rumble.png",
            short_description="""Master rugged landings in wild terrain.""",
            long_description="""Land where roads fear to go. Fly low, touch down rough, and master short-field takeoffs in rugged terrain. For those who think airports are for amateurs.""",
            available_aircraft="""UH-1 Huey""",
            availability="""Saturday 10am, Wednesday 3pm"""
        ),
        
                Flight(
            slug="tight_wing_tango",
            name="Tight Wing Tango",
            tagline="Formation Flight",
            price=259,
            image="tight_wing_tango.png",
            short_description="""Fly in close formation like a real air show team.""",
            long_description="""Strap in and get cozy — this is precision flying with wingtip intimacy. Fly tight, fly proud, and keep it together like your life depends on it (because it kinda does).""",
            available_aircraft="""F-4 Phantom, L-39C Albatros""",
            availability="""Tuesday 10am, Tuesday 6pm, Thursday 3pm"""
        ),
        
                Flight(
            slug="blind_but_brave",
            name="Blind but Brave",
            tagline="IFR Bootcamp",
            price=279,
            image="blind_but_brave.png",
            short_description="""Train like the pros with full instrument-only flying.""",
            long_description="""Clouds? Darkness? Who needs eyes when you've got instruments. Learn to fly without visuals and trust your panel like it's your co-pilot""",
            available_aircraft="""Cirrus SR20, Piper Warrior PA2""",
            availability="""Friday 11pm, Saturday 11pm"""
        ),
        
                Flight(
            slug="smooth_cruise",
            name="Smooth Cruise",
            tagline="Scenic Soarer",
            price=199,
            image="smooth_cruise.png",
            short_description="""Relaxing panoramic flight over Berry and beyond.""",
            long_description="""Chill vibes only. Glide over Berry's fictional countryside in a laid-back tour that's more vibes than velocity. Great for romantics, Instagrammers, and dads who snore in Cessnas.""",
            available_aircraft="""Cessna 182T""",
            availability="""Monday 12pm, Tuesday 12pm, Wednesday 12pm, Thursday 12pm"""
        ),
        
                Flight(
            slug="Double_Trouble",
            name="Double Trouble",
            tagline="Twin Engine Masterclass",
            price=289,
            image="double_trouble.png",
            short_description="""Two engines, double the power and complexity.""",
            long_description="""Twice the engines, twice the stress. Manage power, redundancy, and drama in this twin-engine trial-by-fire. Only for future captains and caffeine addicts.""",
            available_aircraft="""Beechcraft Baron B55, F-14B Tomcat""",
            availability="""Thursday 4pm, Friday 4pm"""
        ),
        
                Flight(
            slug="midnight_buzz",
            name="Midnight Buzz",
            tagline="Night Owl Flight",
            price=249,
            image="midnight_buzz.png",
            short_description="""Experience the skies after dark in this nighttime thrill.""",
            long_description="""See the world lit up like a Christmas tree. This night training adventure is equal parts beautiful and butt-clenching. Stars, strobes, and just enough darkness to keep things interesting.""",
            available_aircraft="""Beechcraft Baron B55""",
            availability="""Saturday 3am, Sunday 3am"""
        ),
        
                Flight(
            slug="danger_close",
            name="Danger Close",
            tagline="CAS Combat Simulation",
            price=299,
            image="danger_close.png",
            short_description="""Call in the danger zone with close air support drills.""",
            long_description="""Fly low, fly fast, and support fictional ground troops in Close Air Support training. Simulated bombs, screaming runs — pew pew included.""",
            available_aircraft="""Mirage F-1, Super Tucano, L-39C Albatros""",
            availability="""Monday 2pm, Thursday 2pm, Friday 2pm"""
        ),
        
                Flight(
            slug="sky_patrol",
            name="Sky Patrol",
            tagline="CAP Combat Simulation",
            price=289,
            image="sky_patrol.png",
            short_description="""Fly a fighter patrol and intercept intruders.""",
            long_description="""Take to the skies for Combat Air Patrol simulation — patrol the perimeter, intercept enemy bogeys, and defend Ray's Airfield like the 80s never ended.""",
            available_aircraft="""Mirage F-1 , F-14B Tomcat , F-4 Phantom""",
            availability="""Monday 10am, Tuesday 10am, Wednesday 10am"""
        ),
        
                Flight(
            slug="teach_the_sky",
            name="Teach the Sky Instructor Flight",
            tagline="Teach the Sky",
            price=259,
            image="teach_the_sky.png",
            short_description="""Get a taste of instructing in this mentoring mission.""",
            long_description="""Ready to boss others around in the cockpit? This flight is for budding instructors ready to turn their nagging into a certification.""",
            available_aircraft="""F-4 Phantom""",
            availability="""Wednesday 9am"""
        ),
        
                Flight(
            slug="final_boss",
            name="Flight School Final Boss",
            tagline="CPL Training",
            price=399,
            image="final_boss.png",
            short_description="""The big league. Everything you need for commercial wings.""",
            long_description="""The big league. Everything you need to earn those commercial wings. If you're serious about flying for money — this is your launchpad.""",
            available_aircraft="""Cirrus SR20, Piper Warrior PA2""",
            availability="""Friday 6pm"""
        ),
        
                Flight(
            slug="weekend_warrior",
            name="Weekend Warrior",
            tagline="RPL Express",
            price=229,
            image="weekend_warrior.png",
            short_description="""Knock out your recreational pilot certificate in a weekend""",
            long_description="""Learn to fly for the joy of it. Perfect for hobbyists, enthusiasts, and Top Gun fans who haven't told their partner they're doing this yet.""",
            available_aircraft="""Beechcraft Baron B55, King Air C90GTi, UH-1 Huey""",
            availability="""Saturday 3pm, Sunday 3pm"""
        ),
        
                Flight(
            slug="bat_out_of_hell",
            name="Bat Out of Hell",
            tagline="Jet Fighter Rampage",
            price=319,
            image="bat_out_of_hell.png",
            short_description="""Raw speed. Pure adrenaline. Be the missile.""",
            long_description="""Strap into a supersonic beast and become the missile. Max afterburner, hard turns, and serious power. Not for the faint of heart — or the legally cautious.""",
            available_aircraft="""F-14B Tomcat""",
            availability="""Friday 8pm, Saturday 7pm"""
        ),
        
                Flight(
            slug="love_above",
            name="Love Above",
            tagline="Romantic Sky Stroll",
            price=219,
            image="love_above.png",
            short_description="""A scenic flight for two—romance in the clouds.""",
            long_description="""Sweep someone off their feet — literally. A smooth, scenic cruise with a touch of charm. Champagne optional. Cheesy love songs absolutely included.""",
            available_aircraft="""King Air C90GTi""",
            availability="""Friday 9pm, Saturday 10am, Saturday 9m"""
        ),
        
                Flight(
            slug="zero_chill",
            name="Zero Chill",
            tagline="Advanced Aero Slam",
            price=299,
            image="zero_chill.png",
            short_description="""Advanced maneuvers to test your nerve and precision.""",
            long_description="""Take your aerobatics up a notch. Extreme maneuvers, zero-G moments, and lots of screaming. For veterans of "Roll & Rumble" only.""",
            available_aircraft="""Boeing Stearman ,  Pitts Special S2B""",
            availability="""Monday 6pm, Tuesday 3pm"""
        ),
        
                Flight(
            slug="sky_float",
            name="Sky Float",
            tagline="Cruisy Snooze Flight",
            price=199,
            image="sky_float.png",
            short_description="""Laid-back lift with minimal Gs and maximum chill.""",
            long_description="""Kick back and let the wind do the work. Think hammock in the clouds. Comes with optional pilot nap mode and dad jokes.""",
            available_aircraft="""Cessna 182T""",
            availability="""Wednesday 12pm, Wednesday 5pm"""
        )
    ]

    for flight in flights:
        db.session.add(flight)
    db.session.flush()

# Link aircraft to flights
    flight = Flight.query.filter_by(slug="danger_close").first()
    aircraft = aircraft_by_slug.get("mirage_f1")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="sky_patrol").first()
    aircraft = aircraft_by_slug.get("mirage_f1")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="smooth_cruise").first()
    aircraft = aircraft_by_slug.get("cessna_182t")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="weekend_warrior").first()
    aircraft = aircraft_by_slug.get("cessna_182t")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="roll_rumble").first()
    aircraft = aircraft_by_slug.get("boeing_stearman")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="zero_chill").first()
    aircraft = aircraft_by_slug.get("boeing_stearman")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="Double_Trouble").first()
    aircraft = aircraft_by_slug.get("beechcraft_baron")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="sky_patrol").first()
    aircraft = aircraft_by_slug.get("f_14b_tomcat")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="bat_out_of_hell").first()
    aircraft = aircraft_by_slug.get("f_14b_tomcat")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="Double_Trouble").first()
    aircraft = aircraft_by_slug.get("king_air")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="weekend_warrior").first()
    aircraft = aircraft_by_slug.get("king_air")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="love_above").first()
    aircraft = aircraft_by_slug.get("king_air")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="danger_close").first()
    aircraft = aircraft_by_slug.get("super_tucano")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="roll_rumble").first()
    aircraft = aircraft_by_slug.get("super_tucano")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="rough_strip_rumble").first()
    aircraft = aircraft_by_slug.get("uh_1 huey")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="weekend_warrior").first()
    aircraft = aircraft_by_slug.get("uh_1 huey")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="blind_but_brave").first()
    aircraft = aircraft_by_slug.get("cirrus_sr20")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="final_boss").first()
    aircraft = aircraft_by_slug.get("cirrus_sr20")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="roll_rumble").first()
    aircraft = aircraft_by_slug.get("pitts_special")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="zero_chill").first()
    aircraft = aircraft_by_slug.get("pitts_special")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="final_boss").first()
    aircraft = aircraft_by_slug.get("piper_warrior")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="blind_but_brave").first()
    aircraft = aircraft_by_slug.get("piper_warrior")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="teach_the_sky").first()
    aircraft = aircraft_by_slug.get("f_4phantom")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="sky_patrol").first()
    aircraft = aircraft_by_slug.get("f_4phantom")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="tight_wing_tango").first()
    aircraft = aircraft_by_slug.get("f_4phantom")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="tight_wing_tango").first()
    aircraft = aircraft_by_slug.get("l_39c_albatros")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="danger_close").first()
    aircraft = aircraft_by_slug.get("l_39c_albatros")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    flight = Flight.query.filter_by(slug="sky_float").first()
    aircraft = aircraft_by_slug.get("cessna_182t")
    if flight and aircraft:
        flight.aircraft.append(aircraft)

    db.session.commit()
    print("✅ Database seeded with aircraft and flights.")

