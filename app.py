import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Stations = Base.classes.station
session = Session(engine)



app = Flask(__name__)

@app.route("/")
def homepage():
<<<<<<< HEAD
    """List all available api routes."""
=======
    """List all available api routes. """
>>>>>>> 484f926254c4977d29cf871196f3a48a052dbe86
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/<"
        f"/api/v1.0/stations<br/<"
        f"/api/v1.0/tobs<br/<"
        f"new text"
    )

@app.route("/api/v1.0/precipitation")
def measurement():

    """Return precipitation and dates as a dictionary"""
    #Query 
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    climate_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= start_date).\
    order_by(Measurement.date).all()

    # Create a dictionary using date as the key and prcp as the value
    climate_dict = dict(climate_data)
    climate_analysis = pd.DataFrame({'Precipitation': climate_dict})
<<<<<<< HEAD
    climate_analysis_df = climate_analysis.to_json()
    
    return jsonify(climate_analysis_df)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Stations.station).all()

    # Unravel results into a 1D array and convert to a list
    stations = list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temp_obs():
    """Return dates and temps from most active station from the last year"""
    start_date2 = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    tobs_query = session.query(Measurement.station,Measurement.date, Measurement.tobs).\
         filter(Measurement.station == 'USC00519281').\
         filter(Measurement.date >= start_date2).all()

    tobs = list(np.ravel(tobs_query))
    return jsonify(tobs)


@app.route('/api/v1.0/start_date')
def start():
    start_d = session.query(Measurement.station,Measurement.date,func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= '2017-01-22')
    
    start_date = start_d.to_dict()
    
    return jsonify(start_date)
   
=======

    return jsonify(climate_analysis)

# @app.route("/api/v1.0/stations")
# def Stations():
#     session = Session(engine)
# #quReturn a JSON list of stations from the dataset.


>>>>>>> 484f926254c4977d29cf871196f3a48a052dbe86
if __name__ == '__main__':
    app.run(debug=True, port=8000)