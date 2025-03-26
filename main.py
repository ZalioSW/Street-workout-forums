from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route("/posts")
def posts_page():
    return render_template("posts.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

@app.route("/signupGet")
def signupGet():
    ime = request.args.get("ime")
    geslo = request.args.get("geslo")
    return "dela"

@app.route("/login")
def login_page():
    return render_template("login.html")

app.run(debug=True)