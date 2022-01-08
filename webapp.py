from flask import Flask
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes, url_prefix="/htj") # htj = Hack the Job, can always be changed
app.secret_key = '8f93wn_febiw28983bf3f3983/'

if __name__ == '__main__':
    app.run(debug = True, port=8080)
