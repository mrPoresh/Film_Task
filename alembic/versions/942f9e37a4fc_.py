"""empty message

Revision ID: 942f9e37a4fc
Revises: 
Create Date: 2020-09-01 11:33:28.419980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942f9e37a4fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FilmTable1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('film', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FilmTable1')
    # ### end Alembic commands ###
