from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, Karthik!"


@app.route("/hello/")
def hello():
  return "<p>Hello, World!</p>"


@app.route("/about/")
def about():
  return "<p>This is a About Page</p>"


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
