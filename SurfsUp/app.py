# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# Create connection to Hawaii.sqlite file

engine = create_engine("../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station




#################################################
# Flask Setup
#################################################
# Initialize Flask
app = Flask(__name__)






#################################################
# Flask Routes
#################################################
# Create Flask Routes 
# Create root route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: to access values between a start and end date enter both dates using format: YYYY-mm-dd/YYYY-mm-dd"
    )


@app.route("/api/v1.0/precipitation")
def Precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return annual precipitation data"""
    # query the data
    precipitation_query_results = session.query(Measurement.prcp, Measurement.date).all()


    # Close session
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
        # 1. Create an empty list of precipitation query values 
        # 2. Create for loop to iterate through query results (precipitation_query_results) 
        # 3. Create dictionary with key "precipitation" set to prcp from precipitation_query_results and key "date" to date from precipitation_query_results
        # 4. Append values from precipitation_dict to your original empty list precipitation_query_values 
        # 5. Return JSON format of your new list that now contains the dictionary of prcp and date values to your browser
    
    precipitaton_query_values = []
    for prcp, date in precipitation_query_results:
        precipitation_dict = {}
        precipitation_dict["precipitation"] = prcp
        precipitation_dict["date"] = date
        precipitaton_query_values.append(precipitation_dict)

    return jsonify(precipitaton_query_values) 












