import datetime as dt
import numpy as np
import pandas as pd

# import dependencies needed for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import the Flask dependency
from flask import Flask, jsonify

# set up database engine for the flask app
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the database
Base.prepare(engine, reflect=True)

# save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database
session = Session(engine)

# define a flask app
app = Flask(__name__)

# define the welcome route
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# define precipitation analysis route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    
    # create a variable for the results
    precip = {date: prcp for date, prcp in precipitation}

    # return the results in JSON format
    return jsonify(precip)

# define the stations route
@app.route("/api/v1.0/stations")
def stations():
    # get all of the stations in our database
    results = session.query(Station.station).all()

    # unravel the results into a one-dimensional array 
    # and convert that array into a list
    stations = list(np.ravel(results))

    # return the results in JSON format
    return jsonify(stations=stations)

# define the temperature observations route
@app.route("/api/v1.0/tobs")
def temp_monthly():

    # calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # unravel the results into a one-dimensional array 
    # and convert that array into a list
    temps = list(np.ravel(results))

    # return the results in JSON format
    return jsonify(temps=temps)

# define summary statistics report route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):

    # create a list for minimum, average, and maximum temperatures
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # query the database using the list that we just made
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()

        # unravel the results into a one-dimensional array 
        # and convert that array into a list
        temps = list(np.ravel(results))

        # return the results in JSON format
        return jsonify(temps=temps)

    # calculate the temperature minimum, average, and maximum 
    # with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    # unravel the results into a one-dimensional array 
    # and convert that array into a list
    temps = list(np.ravel(results))

    # return the results in JSON format
    return jsonify(temps=temps)