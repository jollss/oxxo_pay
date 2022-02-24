"""empty message

Revision ID: 59f4787fab93
Revises: 
Create Date: 2022-02-17 14:12:57.222900

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy_utils import UUIDType


# revision identifiers, used by Alembic.
revision = '59f4787fab93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bitacora_pagos_recurrentes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', UUIDType(binary=False), nullable=True),
    sa.Column('recived_data_magneton', sa.Text(length=16777215), nullable=True),
    sa.Column('response_data_conekta', sa.Text(length=16777215), nullable=True),
    sa.Column('status_conekta', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bitacora_pagos_recurrentes')
    # ### end Alembic commands ###
