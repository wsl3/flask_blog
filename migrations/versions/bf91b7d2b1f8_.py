"""empty message

Revision ID: bf91b7d2b1f8
Revises: 38d90fb155e8
Create Date: 2019-03-23 15:47:39.374507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf91b7d2b1f8'
down_revision = '38d90fb155e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tag', 'timestamp')
    # ### end Alembic commands ###
