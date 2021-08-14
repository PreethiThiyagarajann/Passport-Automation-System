from flask import Flask, redirect, url_for, render_template, request
from police_login import *
from admin_login import *
from user_register import *
from find_user import *
from police_verify import *
from admin_verify import *
from user_login import *
from check_status import *
from update_date import *

app = Flask(__name__)

error_code = []


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
        if login_status_police[1] == 0:
            return redirect(url_for("police_user_search"))
        else:
            error_code.clear()
            error_code.append("Access Denied")
            return redirect(url_for("throw_error"))


user_details_police = []


@app.route("/police_user_search", methods=["POST", "GET"])
def police_user_search():
    if request.method == "GET":
        return render_template("police_user_search.html")
        user_details_police.clear()
    else:
        user_id_user = request.form.get('user_id')
        user_exists = find_user(user_id_user)
        user_details_police.append(user_exists)
        if user_exists[1] == 0:
            return redirect(url_for("police_verify"))
        else:
            error_code.clear()
            error_code.append("User does not exist")
            return redirect(url_for("throw_error"))


@app.route("/police_verify", methods=["POST", "GET"])
def police_verify():
    if request.method == "GET":
        return render_template("user_details_display_police.html", user_id=user_details_police[0][0][0],
                               username=user_details_police[0][0][2], address=user_details_police[0][0][6],
                               email=user_details_police[0][0][4], aadhar=user_details_police[0][0][5])
    else:
        if request.form.get('submit_button') == "yes":
            police_verify_status = police_verify_func(user_details_police[0][0][0])
            error_code.clear()
            error_code.append(police_verify_status[0])
            return redirect(url_for("throw_error"))
        else:
            error_code.clear()
            error_code.append("Details not verified")
            return redirect(url_for("throw_error"))


@app.route("/admin_login", methods=["POST", "GET"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_admin = admin_login_func(username, password)
        if login_status_admin[1] == 0:
            return redirect(url_for("admin_user_search"))
        else:
            error_code.clear()
            error_code.append("Access Denied")
            return redirect(url_for("throw_error"))


user_details_admin = []


@app.route("/admin_user_search", methods=["POST", "GET"])
def admin_user_search():
    if request.method == "GET":
        return render_template("admin_user_search.html")
        user_details_admin.clear()
    else:
        user_id_user = request.form.get('user_id')
        user_exists = find_user(user_id_user)
        user_details_admin.append(user_exists)
        if user_exists[1] == 0:
            return redirect(url_for("admin_verify"))
        else:
            error_code.clear()
            error_code.append("User does not exist")
            return redirect(url_for("throw_error"))


@app.route("/admin_verify", methods=["POST", "GET"])
def admin_verify():
    if request.method == "GET":
        return render_template("user_details_display_admin.html", user_id=user_details_admin[0][0][0],
                               username=user_details_admin[0][0][2], address=user_details_admin[0][0][6],
                               email=user_details_admin[0][0][4], aadhar=user_details_admin[0][0][5])
    else:
        if request.form.get('submit_button') == "yes":
            admin_verify_status = admin_verify_func(user_details_admin[0][0][0])
            return redirect(url_for("issue_date"))
        else:
            error_code.clear()
            error_code.append("Details not verified")
            return redirect(url_for("throw_error"))


@app.route("/issue_date", methods=["POST", "GET"])
def issue_date():
    if request.method == "GET":
        return render_template("appointment.html", admin_status=user_details_admin[0][0][7])
    else:
        issue_date_user = request.form.get('birthday')
        update_date(user_details_admin[0][0][0], issue_date_user)
        error_code.clear()
        error_code.append("Date added")
        return redirect(url_for("throw_error"))


@app.route("/user_choices", methods=["POST", "GET"])
def user_choices():
    if request.form.get('submit_button') == "register":
        return redirect(url_for("user_registration"))
    elif request.form.get('submit_button') == "check_status":
        return redirect(url_for("user_login"))
    else:
        return render_template("user_options.html")


@app.route("/user_login", methods=["POST", "GET"])
def user_login():
    if request.method == "GET":
        return render_template("user_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_user = user_login_func(username, password)
        if request.form.get('submit_button') == "proceed":
            return redirect(url_for("login"))
        else:
            if login_status_user[1] == 0:
                user_status_details = check_status_func(username, password)
                return render_template("user_status.html", admin_status=user_status_details[0],
                                       police_status=user_status_details[1], appointment=user_status_details[2])
            else:
                error_code.clear()
                error_code.append("Access Denied")
                return redirect(url_for("throw_error"))


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
        error_code.clear()
        error_code.append(registration_status_user)
        return redirect(url_for("throw_error"))


@app.route("/error_screen", methods=["POST", "GET"])
def throw_error():
    if request.method == "GET":
        return render_template("display_error.html", error=error_code[0])
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
