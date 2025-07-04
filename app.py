from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Welcome to iskolutions"

@app.route("/<name>")
def display_name(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run()