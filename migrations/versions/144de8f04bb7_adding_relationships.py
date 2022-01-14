"""adding relationships

Revision ID: 144de8f04bb7
Revises: c729efbe896a
Create Date: 2022-01-14 08:19:37.778768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '144de8f04bb7'
down_revision = 'c729efbe896a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'author')
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('books', sa.Column('author', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    # ### end Alembic commands ###