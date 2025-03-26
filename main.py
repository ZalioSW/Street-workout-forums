from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from tinydb import TinyDB, Query
db = TinyDB('forum.json')
users = db.table('uporabniki')
posts = db.table('objave')

app = Flask(__name__)

@app.route("/")
def main_page():
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    else:
        return render_template("home.html")

@app.route("/login")
def login_page():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = users.get(User.username == username)
            if user:
                if user['password'] == password:
                    session['username'] = username
                    return jsonify({'success': True})
                else:
                    return jsonify({'success': False, 'error': 'Wrong password'})
            else:
                return render_template('signup.html')
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template("login.html")


@app.route("/posts")
def posts_page():
    return render_template("posts.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")

app.run(debug=True)