from app import app, db
from faker import Faker
from models import Admin, Article, Tag, Info
from random import randint
import click
from time import sleep



@app.cli.command()
def forge():
    db.drop_all()
    db.create_all()

    fake = Faker(locale="zh_CN")


    # Admin model
    admin = Admin(
        username="wsl",
        password="123456"
    )
    db.session.add(admin)
    db.session.commit()

    # tags
    for i in range(10):
        try:
            tag = Tag(
                name = fake.word()
            )

            db.session.add(tag)
        except Exception:
            continue
    db.session.commit()

    # articles
    for i in range(10):
        try:
            article = Article(
                title = fake.sentence(),
                text = fake.text(),
            )
            article.tags.append(Tag.query.get(randint(1, Tag.query.count())))
            db.session.add()
        except Exception:
            continue
    db.session.commit()

    # Info
    blogTitle = "wsl' blog"
    blogSubTitle = "wsdwsd"
    text = "我是来自我是来自我是"
    info = Info()
    db.session.add(info)
    db.session.commit()
    click.echo("Done.")