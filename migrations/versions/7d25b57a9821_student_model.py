"""Student model

Revision ID: 7d25b57a9821
Revises: a0cd0feb8bb9
Create Date: 2022-10-11 19:33:23.974204

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '7d25b57a9821'
down_revision = 'a0cd0feb8bb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identity_document', sa.Unicode(length=255), nullable=False),
    sa.Column('first_name', sa.Unicode(length=255), nullable=False),
    sa.Column('second_name', sa.Unicode(length=255), nullable=True),
    sa.Column('first_surname', sa.Unicode(length=255), nullable=False),
    sa.Column('second_surname', sa.Unicode(length=255), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('identity_document')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
