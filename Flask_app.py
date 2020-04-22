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

app = Flask(__name__)

@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/<"
        f"/api/v1.0/stations<br/<"
        f"/api/v1.0/tobs<br/<"
    )

@app.route("/api/v1.0/precipitation")
def Measurement():
    
    session = Session(engine)

    """Return precipitation and dates as a dictionary"""
    # Query 
    start_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    climate_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= start_date).\
    order_by(Measurement.date).all()

    session.close()

    # Create a dictionary using date as the key and prcp as the value
    climate_dict = dict(climate_data)
    climate_analysis = pd.DataFrame({'Precipitation': climate_dict})

    return jsonify(climate_analysis)

