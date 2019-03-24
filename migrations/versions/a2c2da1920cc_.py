"""empty message

Revision ID: a2c2da1920cc
Revises: edbbd149b2f9
Create Date: 2019-03-23 20:10:20.155558

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a2c2da1920cc'
down_revision = 'edbbd149b2f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('username', sa.String(length=128), nullable=False))
    op.drop_column('admin', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('name', mysql.VARCHAR(length=128), nullable=False))
    op.drop_column('admin', 'username')
    # ### end Alembic commands ###
