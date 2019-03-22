from app import app, db
from flask import render_template, redirect, request, url_for, flash
from models import Admin, Article, Tag, Info



@app.route("/")
@app.route("/<int:id>")
def index(id=0):
    id = id or Article.query.order_by(Article.timestamp.desc())[0].id
    showArticle = Article.query.get(id)
    return render_template("index.html", showArticle=showArticle)


@app.route("/achieve/")
def achieve():
    times = list(set([t.timestamp.year for t in Article.query.all()]))
    times.sort(reverse=True)
    Articles = [{"year": year, "articles": Article.query.filter(Article.timestamp.like(f"%{year}%")).order_by(
        Article.timestamp.desc()).all()} \
                for year in times]

    return render_template("achieve.html", Articles=Articles)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/tagfound/<int:id>")
def searchTag(id):
    FoundTag = Tag.query.get(id)
    Articles = FoundTag.articles

    return render_template("tags.html", Articles=Articles, FoundTag=FoundTag)




@app.errorhandler(404)
def handle_error(e):
    return render_template("404.html")


@app.context_processor
def context_process():
    admin = Admin.query.get(1)
    info = Info.query.get(1)
    tags = Tag.query.all()
    articles = Article.query.order_by(Article.timestamp.desc()).limit(8).all()
    return dict(admin=admin, info=info, tags=tags, articles=articles)


@app.shell_context_processor
def shell_context():
    return dict(db=db, Article=Article, Admin=Admin, Tag=Tag, Info=Info)
