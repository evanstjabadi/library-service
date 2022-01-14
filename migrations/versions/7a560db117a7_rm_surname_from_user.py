"""rm surname from user

Revision ID: 7a560db117a7
Revises: f41dd5e345a3
Create Date: 2022-01-14 08:22:59.847094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a560db117a7'
down_revision = 'f41dd5e345a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'surname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('surname', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
