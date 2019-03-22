from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
@app.route("/<int:id>")
def index(id=0):
    id = id or Article.query.order_by(Article.timestamp.desc())[0].id
    showArticle = Article.query.get(id)
    return render_template("index.html", showArticle=showArticle)

@app.route("/achieve/")
def achieve():
    return render_template("achieve.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.context_processor
def context_process():
    admin = Admin.query.get(1)
    info = Info.query.get(1)
    tags = Tag.query.all()
    articles = Article.query.order_by(Article.timestamp.desc()).all()
    return dict(admin=admin, info=info, tags=tags, articles=articles)

from models import Admin, Article, Tag, Info
from command import forge