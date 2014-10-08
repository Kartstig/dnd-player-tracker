"""create spell table

Revision ID: 24177dfd3f2d
Revises: e3e34d106f7
Create Date: 2014-10-07 22:54:49.702927

"""

# revision identifiers, used by Alembic.
revision = '24177dfd3f2d'
down_revision = 'e3e34d106f7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'spells',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(4000)),
        sa.Column('school', sa.String(50), nullable=False),
        sa.Column('components', sa.String(50), nullable=False),
        sa.Column('level', sa.String(50), nullable=False),
        sa.Column('range', sa.String(50), nullable=False),
        sa.Column('damage', sa.String(50), nullable=False),
        sa.Column('duration', sa.String(50), nullable=False),
        sa.Column('casting_time', sa.String(50), nullable=False),
        sa.Column('area', sa.String(50), nullable=False),
        sa.Column('saving_throw', sa.String(50), nullable=False),
        sa.Column('is_reversible', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
        )


def downgrade():
    op.drop_table('spells')
