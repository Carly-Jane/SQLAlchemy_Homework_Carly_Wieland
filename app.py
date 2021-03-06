# Step 2 - Climate App

# Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

#     Use Flask to create your routes.

# Routes

#     /

#         Home page.

#         List all routes that are available.

#     /api/v1.0/precipitation

#         Convert the query results to a dictionary using date as the key and prcp as the value.

#         Return the JSON representation of your dictionary.

#     /api/v1.0/stations
#         Return a JSON list of stations from the dataset.

#     /api/v1.0/tobs

#         Query the dates and temperature observations of the most active station for the last year of data.

#         Return a JSON list of temperature observations (TOBS) for the previous year.

#     /api/v1.0/<start> and /api/v1.0/<start>/<end>

#         Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#         When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

#         When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

# ________________________________________________________________________________________
# DRAFT FLASK API FROM CLASS ACTIVITY #
# ________________________________________________________________________________________
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

## ABOVE THIS SECTION SHOULD BE COMPLETE ##
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


@app.route("/api/v1.0/names")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Passenger.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/passengers")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)