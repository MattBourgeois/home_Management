from flask import Flask, render_template, redirect, request, session
from Flask_app import app
from Flask_app.models.model import Person

@app.route("/maintenance")
def maintenance_request():
	return render_template("Maintenance.html")


@app.route("/maint", methods = ["POST"])
def send_request():
	pass