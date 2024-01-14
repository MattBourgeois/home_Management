from Flask_app.config.mysqlconnection import connectToMySQL

class House:
	db_name = 'Home_management'
	def __init__(self, data):
		self.id = data["id"]
		self.Name = data["Name"]
		self.Address = data["Address"]
		self.DaysRented = data["DaysRented"] # rented/non
		self.ServiceRequest = data["ServiceRequest"]
		self.Created_at	= data["Created_at"]
		self.Updated_at = data["Updated_at"]
		self.user = None


		@classmethod
		def add_house(cls, data):
			query = "Insert INTO Homes (Name, Address, DaysRented, ServiceRequest, User_id) VALUES (%(Names)s, %(Address)s, %(DaysRented)s, %(ServiceRequest)s, %(User_id)s);"
			return connectToMySQL(cls.db_name).query_db(query, data)