"""Representative model

Revision ID: 1823b06c8d8d
Revises: 7d25b57a9821
Create Date: 2022-10-13 13:42:20.305159

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '1823b06c8d8d'
down_revision = '7d25b57a9821'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('representative',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identity_document', sa.Unicode(length=255), nullable=False),
    sa.Column('first_name', sa.Unicode(length=255), nullable=False),
    sa.Column('second_name', sa.Unicode(length=255), nullable=True),
    sa.Column('first_surname', sa.Unicode(length=255), nullable=False),
    sa.Column('second_surname', sa.Unicode(length=255), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('identity_document')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('representative')
    # ### end Alembic commands ###
