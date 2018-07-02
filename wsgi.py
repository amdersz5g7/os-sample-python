from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/mars")
def hello_mars():
    return "Hello Mars --message from world!"

if __name__ == "__main__":
    application.run()
