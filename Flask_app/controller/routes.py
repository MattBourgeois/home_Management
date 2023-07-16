from flask import Flask, render_template, redirect, request, session
from Flask_app import app

@app.route("/")
def index():
	booked_dates = ['2023-07-18', '2023-07-19', '2023-07-25', '2023-07-26']
	return render_template("index.html", booked_dates=booked_dates)