"""empty message

Revision ID: c49a07b9e55b
Revises: 74cba1028de3
Create Date: 2021-04-19 04:59:09.282399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c49a07b9e55b'
down_revision = '74cba1028de3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('name', sa.String(length=50), nullable=True))
    op.drop_column('favorites', 'tipo')
    op.drop_column('favorites', 'favorite_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('favorite_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('favorites', sa.Column('tipo', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('favorites', 'name')
    # ### end Alembic commands ###