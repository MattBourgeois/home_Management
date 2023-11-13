from flask import Flask

app = Flask(__name__)

app.secret_key = "test"


# Add a database for requests, many to many,
#add a calander to show when requests were inputted and when/if they got finished