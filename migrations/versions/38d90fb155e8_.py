"""empty message

Revision ID: 38d90fb155e8
Revises: ed9537ccb340
Create Date: 2019-03-23 15:27:38.306784

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '38d90fb155e8'
down_revision = 'ed9537ccb340'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tag', 'name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    op.create_unique_constraint(None, 'tag', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='unique')
    op.alter_column('tag', 'name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###
