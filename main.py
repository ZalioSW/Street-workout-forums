from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from tinydb import TinyDB, Query
db = TinyDB('forum.json')
users = db.table('uporabniki')
posts = db.table('objave')

app = Flask(__name__)
app.secret_key = "zaliosw_najjaci123"

@app.route("/")
def main_page():
    if 'username' in session:
        return render_template("home.html", username=session['username'])
    else:
        return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            User = Query()
            user = users.search(User.username == username)
            if user:
                if user[0]['password'] == password:
                    session['username'] = username
                    return jsonify({'success': True})
                else:
                    return jsonify({'success': False, 'error': 'Wrong password'})
            else:
                return jsonify({'success': False, 'error': 'User not found. Please sign up.'})
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            users.insert({'username': username, 'password': password})
            session['username'] = username
            return jsonify({'success': True})
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template("signup.html")

@app.route("/logout")
def logout_page():
    session.pop('username', None)
    return redirect(url_for('login_page'))

@app.route("/posts")
def posts_page():
    return render_template("posts.html")

app.run(debug=True)