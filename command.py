from app import app, db
from faker import Faker
from models import Admin, Article, Tag, Info
from random import randint
import click



@app.cli.command()
def forge():
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

    click.echo("Done.")