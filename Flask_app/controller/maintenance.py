from flask import Flask, render_template, redirect, request, session
from Flask_app import app
from Flask_app.models.model import Person
from Flask_app.controller import routes
from Flask_app.models.home import *

@app.route("/maintenance")
def maintenance_request():
	return render_template("Maintenance.html")


@app.route("/maint", methods = ["POST"])
def send_request():
	data = {
		"Name": request.form["Name"],
		"Address": request.form["Address"],
		"ServiceRequest": request.form["ServiceRequest"]
	}
	save_request(data)
	return redirect("/dash")