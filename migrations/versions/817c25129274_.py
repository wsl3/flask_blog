"""empty message

Revision ID: 817c25129274
Revises: 3beb38a36b25
Create Date: 2019-03-23 16:40:45.475450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '817c25129274'
down_revision = '3beb38a36b25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'timestamp')
    # ### end Alembic commands ###
