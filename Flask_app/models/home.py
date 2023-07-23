from Flask_app.config.mysqlconnection import connectToMySQL

class House:
	db_name = 'Home_management'
	def __init__(self, data):
		self.id = data["id"]
		self.Name = data["Name"]
		self.Address = data["Address"]
		self.DaysRented = data["DaysRented"]
		self.ServiceRequest = data["ServiceRequest"]
		self.Created_at	= data["Created_at"]
		self.Updated_at = data["Updated_at"]
		self.user = None

		@classmethod
		def save_request(cls, data):
			query = "INSTER INTO Home_management (Name, Address, ServiceRequest) VALUES (%(Name)s, %(Address)s, %(ServiceRequest)s);"
			return connectToMySQL(cls, db_name).query_db(query, data)