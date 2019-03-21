from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    tags = Tag.query.all()
    articles = Article.query.all()
    return render_template("base.html", tags=tags, articles=articles)

@app.route("/achieve/")
def achieve():
    return render_template("achieve.html")

@app.route("/about/")
def about():
    return render_template("about.html")

from models import Admin, Article, Tag, Info
from command import forge