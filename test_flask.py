from flask import Flask, redirect, url_for, render_template, request
from police_login import *
from admin_login import *
from user_register import *

app = Flask(__name__)


@app.route("/")
def hello():
    exec(open('setup.py').read())
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form.get('submit_button') == "police":
        return redirect(url_for("police_login"))
    elif request.form.get('submit_button') == "admin":
        return redirect(url_for("admin_login"))
    elif request.form.get('submit_button') == "user":
        return redirect(url_for("user_choices"))
    else:
        return render_template("index.html")


@app.route("/police_login", methods=["POST", "GET"])
def police_login():
    if request.method == "GET":
        return render_template("police_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_police = police_login_func(username, password)
        return f"{login_status_police[0]}"


@app.route("/admin_login", methods=["POST", "GET"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_admin = admin_login_func(username, password)
        return f"{login_status_admin[0]}"


@app.route("/user_choices", methods=["POST", "GET"])
def user_choices():
    if request.form.get('submit_button') == "register":
        return redirect(url_for("user_registration"))
    elif request.form.get('submit_button') == "check_status":
        return f"""<html>
	<link rel="stylesheet" href="/static/style_login_admin.css" type="text/css">
		<form action="/admin_login" method="POST">
			<div class="login">
				<div class="login-screen">
					<div class="app-title">
						<h1>Admin Login</h1>
					</div>
				<div class="login-form">
					<div class="control-group">
						<input type="text" class="login-field" placeholder="usernmane" name="username">
						<label class="login-field-icon fui-user" for="login-name"></label>
					</div>
					<div class="control-group">
						<input type="password" class="login-field" placeholder="password" name="password">
						<label class="login-field-icon fui-lock" for="login-pass"></label>
					</div>
					<input type="submit" value="Log in" class="btn btn-primary btn-large btn-block">
				</div>
				</div>
			</div>
		</form>
</html>
"""
    else:
        return render_template("user_options.html")


@app.route("/user_registration", methods=["POST", "GET"])
def user_registration():
    if request.method == "GET":
        return render_template("user_registration.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        aadhar = request.form.get("aadhar")
        address = request.form.get("address")
        choice = request.form.get("reg")
        registration_status_user = user_register(username, password, email, aadhar, address, choice)
        return f"{registration_status_user}"


if __name__ == "__main__":
    app.run(debug=True)
