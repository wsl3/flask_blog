from app import app, db
from faker import Faker
from models import Admin, Article, Tag, Info
from random import randint
import click
from time import sleep


@app.cli.command()
@click.option("--tags", default=10, help="produce tags")
@click.option("--articles", default=10, help="produce articles")
def forge(tags, articles):
    db.drop_all()
    db.create_all()

    fake = Faker(locale="zh_CN")

    # tags
    for i in range(tags):
        try:
            tag = Tag(
                name=fake.word()
            )

            db.session.add(tag)
        except Exception:
            continue
    db.session.commit()

    # articles
    for i in range(articles):
        try:
            article = Article(
                title=fake.sentence(),
                text=fake.text(),
            )
            article.tags.append(Tag.query.get(randint(1, Tag.query.count())))
            db.session.add()
        except Exception:
            continue
    db.session.commit()

    info = Info()
    db.session.add(info)
    db.session.commit()
    click.echo("Done.")


@app.cli.command()
def rebuild():
    db.drop_all()
    db.create_all()


@app.cli.command()
def admin():
    admin = Admin(
        username="wsl",
        password="666"
    )
    db.session.add(admin)
    db.session.commit()
