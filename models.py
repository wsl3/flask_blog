from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

association_table = db.Table("association", db.Column("article_id", db.Integer, db.ForeignKey("article.id")),
                             db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")))


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, default="admin")
    password_hash = db.Column(db.String(450), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __repr__(self):
        return f"Admin<{self.username}>"


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False, index=True)
    text = db.Column(db.TEXT)
    author = db.Column(db.String(500), default="wsl")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    tags = db.relationship("Tag", secondary=association_table, back_populates="articles")

    def __repr__(self):
        return f"Article< id: {self.id} title: {self.title}>"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), unique=True, default="Default")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    articles = db.relationship("Article", secondary=association_table, back_populates="tags")

    def __repr__(self):
        return f"Tag< {self.name} >"


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogTitle = db.Column(db.String(1500), nullable=False, default="WSL' Blog")
    blogSubTitle = db.Column(db.String(2000), nullable=False,
                             default="We slept on the floor We waded through the river !")
    text = db.Column(db.Text)  # About中的文本
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Info< {self.bolgTitle} >"


