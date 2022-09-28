"""Initial migration

Revision ID: 32a2b49737d4
Revises: 
Create Date: 2022-09-28 09:54:04.512298

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '32a2b49737d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Unicode(length=255), nullable=False),
    sa.Column('second_name', sa.Unicode(length=255), nullable=True),
    sa.Column('first_surname', sa.Unicode(length=255), nullable=False),
    sa.Column('second_surname', sa.Unicode(length=255), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
