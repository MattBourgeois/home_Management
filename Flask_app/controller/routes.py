from flask import Flask, render_template, redirect, request, session
from Flask_app import app

@app.route("/")
def index():
	# return render_template("login.html") this will be back once i finsih login mysql
	return render_template("dashboard.html")