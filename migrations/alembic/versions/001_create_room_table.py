"""create room table

Revision ID: 001
Revises:
Create Date: 2023-06-18  # Data de criação da migração

"""
from alembic import op
import sqlalchemy as sa


revision = '001'
down_revision = None


def upgrade():
    op.create_table(
        'room',
        sa.Column('id', sa.BINARY(16), nullable=False),
        sa.Column('number', sa.Integer(), nullable=False),
        sa.Column('available', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        if_not_exists=True
    )


def downgrade():
    op.drop_table('room')


