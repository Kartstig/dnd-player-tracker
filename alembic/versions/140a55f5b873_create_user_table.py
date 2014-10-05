"""create user table

Revision ID: 140a55f5b873
Revises: None
Create Date: 2014-10-01 21:38:27.188221

"""

# revision identifiers, used by Alembic.
revision = '140a55f5b873'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(60)),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('phone_number', sa.String(15)),
        sa.Column('role', sa.Enum('user', 'admin', 'operator'), default='user', nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.UniqueConstraint('username', name='ux_username')
        )


def downgrade():
    op.drop_table('users')
