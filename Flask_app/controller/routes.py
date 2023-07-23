from flask import Flask, render_template, redirect, request, session, flash
from Flask_app import app
from Flask_app.models.model import Person
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def dash():
	return render_template("login.html") 

@app.route("/Register", methods = ["POST"])
def Reg():
	data = {
		"First_name": request.form["First_name"],
		"Last_name": request.form["Last_name"],
		"Email": request.form["Email"],
		"Password": bcrypt.generate_password_hash(request.form["Password"])
	}
	id = User.save(data)
	session['user_id'] = id
	return redirect("/dash")

@app.route("/Login", methods = ["POST"])
def Login():
	user = Person.get_by_email(request.form)
	if not bcrypt.check_password_hash(user.Password, request.form["Password"]):
		flash("Incorrect Email or Password!")
		return redirect('/')
	session["user_id"] = user.id
	print(session["user_id"])
	return redirect("/dash")

@app.route("/Logout")
def Logout():
	session.clear()
	return redirect('/')

@app.route("/dash")
def dashboard():
	return render_template("dashboard.html")

@app.route("/account")
def My_account():
	user = Person.get_by_id(session['user_id'])
	return render_template("account.html", user = user)

