"""Representative model

Revision ID: 0fd046efb93d
Revises: e5b87e176167
Create Date: 2022-10-14 00:07:40.472532

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0fd046efb93d'
down_revision = 'e5b87e176167'
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
    sa.Column('sex', sa.Enum('FEMALE', 'MALE', name='sex'), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_representative')),
    sa.UniqueConstraint('email', name=op.f('uq_representative_email')),
    sa.UniqueConstraint('identity_document', name=op.f('uq_representative_identity_document'))
    )
    op.add_column('student', sa.Column('representative_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_student_representative_id_representative'), 'student', 'representative', ['representative_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_student_representative_id_representative'), 'student', type_='foreignkey')
    op.drop_column('student', 'representative_id')
    op.drop_table('representative')
    # ### end Alembic commands ###
