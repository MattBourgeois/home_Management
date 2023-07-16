from flask import Flask, render_template, redirect, request, session
from Flask_app import app

@app.route("/")
def index():
	return render_template("login.html")
	# return render_template("index.html", booked_dates=booked_dates)