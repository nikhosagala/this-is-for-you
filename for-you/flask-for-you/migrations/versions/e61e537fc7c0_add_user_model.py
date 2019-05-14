"""Add user model

Revision ID: e61e537fc7c0
Revises: d9d194ae5600
Create Date: 2019-04-29 09:36:06.539616

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e61e537fc7c0'
down_revision = 'd9d194ae5600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('modified', sa.DateTime(), nullable=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###