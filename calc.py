import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Server parameters
CLIENT_SIDE_URL = "http://18.216.149.158"
PORT = 8080

@app.route("/")
def index():
    return render_template("calc.html")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, threaded=True, port=PORT)
    app.run(host="localhost", debug=True, port=PORT)
