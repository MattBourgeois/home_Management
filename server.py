from Flask_app import app
from Flask_app.controller import routes, maintenance

if __name__ == "__main__":
	app.run(debug = True, port = 5001)