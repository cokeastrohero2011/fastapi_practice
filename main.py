from flask import Flask

data= []

app = Flask(__name__)

@app.route("/flask_health_check", methods = ["GET"])
def flask_health_check():
    return "Flask is running properly"

app.run(port=8080,debug=True)