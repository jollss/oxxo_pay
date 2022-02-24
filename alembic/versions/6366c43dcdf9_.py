"""empty message

Revision ID: 6366c43dcdf9
Revises: 59f4787fab93
Create Date: 2022-02-17 16:21:41.009239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6366c43dcdf9'
down_revision = '59f4787fab93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('user_id', table_name='bitacora_pagos_recurrentes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('user_id', 'bitacora_pagos_recurrentes', ['user_id'], unique=False)
    # ### end Alembic commands ###
