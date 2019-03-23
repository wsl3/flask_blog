from app import app, login_manager, db
from models import Admin, Article, Tag, Info
from flask_login import login_required, login_user, logout_user
from flask import render_template, redirect, request, url_for, flash, session
from datetime import datetime

@app.route("/login/", methods=["GET", "POST"])
def login():
    admin = Admin.query.get(1)
    if session.get("admin", None):
        return redirect(url_for("admin"))
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        print("admin.username:        {}  ".format(admin) )
        if admin.username == username and admin.check_password(pwd):
            flash("login in successfully!")
            session["admin"] = admin.username
            login_user(admin)
            return redirect(url_for("admin"))

        else:
            flash("用户名或密码错误")
            return redirect(url_for("login"))


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    del session["admin"]
    return redirect(url_for("index"))


@login_manager.user_loader
def user_load(id):
    return Admin.query.get(id)


@app.route("/admin/", methods=["GET", "POST"])
@login_required
def admin():
    return render_template("admin/index.html")


@app.route("/tags_list/")
@login_required
def tags_list():
    return render_template("admin/tags_list.html")


@app.route("/tag_add/", methods=["GET", "POST"])
@login_required
def tag_add():
    if request.method == "POST":
        tag = request.form.get("tag")
        if not Tag.query.filter_by(name=tag).first():
            t = Tag(name=tag)
            db.session.add(t)
            db.session.commit()
            return redirect(url_for("tags_list"))
    return render_template("admin/tag_add.html")


@app.route("/tag_delete/<int:id>")
@login_required
def tag_delete(id):
    tag = Tag.query.get(id)
    db.session.delete(tag)
    db.session.commit()
    return redirect(url_for("tags_list"))


@app.route("/articles_list/")
@login_required
def articles_list():
    return render_template("admin/articles_list.html")


@app.route("/article_add/", methods=["GET", "POST"])
@login_required
def article_add():
    if request.method == "POST":
        tags = request.form.getlist("tag")
        title = request.form.get("title")
        author = request.form.get("author") or "wsl"
        text = request.form.get("text")

        if title and text and tags:

            article = Article(
                title=title,
                text=text,
                author=author
            )
            try:
                for tag in tags:
                    t = Tag.query.filter_by(name=tag).first()
                    article.tags.append(t)

                db.session.add(article)
                db.session.commit()
            finally:
                return redirect(url_for("articles_list"))

    return render_template("admin/article_add.html")


@app.route("/change_pwd/", methods=["GET", "POST"])
@login_required
def change_pwd():
    if request.method == "POST":
        admin = Admin.query.get(1)
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        newpwd = request.form.get("newpwd")
        if admin.check_password(pwd):
            admin.username = username or admin.username
            admin.password = newpwd
            db.session.add(admin)
            db.session.commit()
            return redirect(url_for("admin"))

    return render_template("admin/change_pwd.html")

@app.route("/change_info", methods=["GET", "POST"])
@login_required
def change_info():
    if request.method == "POST":
        info = Info.query.get(1)
        info.blogTitle = request.form.get("title") or info.blogTitle
        info.blogSubTitle = request.form.get("subtitle") or info.blogSubTitle
        info.text = request.form.get("info")

        db.session.add(info)
        db.session.commit()
        return redirect(url_for("about"))
    return render_template("admin/change_info.html")