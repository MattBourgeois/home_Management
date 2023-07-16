from Flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from Flask import flash

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
