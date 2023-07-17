from Flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Person:
	db_name = 'Home_management'
	def __init__(self, data):
		self.id = data["id"]
		self.First_name = data["First_name"]
		self.Last_name = data["Last_name"]
		self.Email = data["Email"]
		self.Password = data["Password"]
		self.Created_at = data["Created_at"]
		self.Updated_at = data["Updated_at"]
		self.user_id = None

	@classmethod
	def save_user(cls, data):
		query = "INSERT INTO Users (First_name, Last_name, Email, Password) VALUES(%(First_name)s, %(Last_name)s, %(Email)s, %(Password)s);"
		return connectToMySQL(cls.db_name).query_db(query, data)

	@classmethod
	def get_by_email(cls, data):
		query = "SELECT * FROM Users WHERE Email = %(Email)s;"
		results = connectToMySQL(cls.db_name).query_db(query, data)
		return cls(results[0])
	
	@classmethod
	def get_by_id(cls, data):
		data = {
			'id': 1
		}
		query = "SELECT * FROM Users WHERE id = %(id)s;"
		results = connectToMySQL(cls.db_name).query_db(query, data)
		print(results)
		return cls(results[0])