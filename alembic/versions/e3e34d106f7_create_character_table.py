"""create character table

Revision ID: e3e34d106f7
Revises: 2342fa857595
Create Date: 2014-10-01 22:07:17.095317

"""

# revision identifiers, used by Alembic.
revision = 'e3e34d106f7'
down_revision = '2342fa857595'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'characters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('xp', sa.Integer, nullable=False),
        sa.Column('level', sa.Integer),
        sa.Column('strength', sa.Integer, nullable=False),
        sa.Column('dexterity', sa.Integer, nullable=False),
        sa.Column('constitution', sa.Integer, nullable=False),
        sa.Column('intelligence', sa.Integer, nullable=False),
        sa.Column('wisdom', sa.Integer, nullable=False),
        sa.Column('charisma', sa.Integer, nullable=False),
        sa.Column('sex', sa.Enum('M','F'), nullable=False),
        sa.Column('alignment', sa.String(50), nullable=False),
        sa.Column('behavior', sa.String(50), nullable=False),
        sa.Column('height', sa.Integer, nullable=False),
        sa.Column('weight', sa.Integer, nullable=False),
        sa.Column('hair_color', sa.String(50), nullable=False),
        sa.Column('age', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('race_id', sa.Integer, 
            sa.ForeignKey('races.id'), nullable=False),
        sa.Column('user_id', sa.Integer, 
            sa.ForeignKey('users.id'), nullable=False),
        )


def downgrade():
    op.drop_table('characters')
