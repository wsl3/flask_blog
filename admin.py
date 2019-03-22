from app import app, login_manager
from models import Admin, Article, Tag, Info
from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, request, url_for, flash

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        admin = Admin.query.get(1)

        if admin.username==username and admin.check_password(pwd):
            flash("login in successfully!")
            login_user(admin)

            return redirect(url_for("admin"))

        else:
            flash("用户名或密码错误")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@login_manager.user_loader
def user_load(id):
    return Admin.query.get(id)


@app.route("/admin/")
def admin():
    return render_template("admin/admin.html")