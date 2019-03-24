"""empty message

Revision ID: ed9537ccb340
Revises: 336db82c04ee
Create Date: 2019-03-22 13:07:28.808394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ed9537ccb340'
down_revision = '336db82c04ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info', sa.Column('blogSubTitle', sa.String(length=600), nullable=False))
    op.drop_column('info', 'bolgSubTitle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('info', sa.Column('bolgSubTitle', mysql.VARCHAR(length=600), nullable=False))
    op.drop_column('info', 'blogSubTitle')
    # ### end Alembic commands ###
