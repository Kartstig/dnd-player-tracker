"""create race table

Revision ID: 2342fa857595
Revises: 140a55f5b873
Create Date: 2014-10-01 21:51:39.569339

"""

# revision identifiers, used by Alembic.
revision = '2342fa857595'
down_revision = '140a55f5b873'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'races',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('sub_race', sa.String(50)),
        sa.Column('lore', sa.String(4000)),
        sa.Column('strength', sa.Integer, nullable=False),
        sa.Column('dexterity', sa.Integer, nullable=False),
        sa.Column('constitution', sa.Integer, nullable=False),
        sa.Column('intelligence', sa.Integer, nullable=False),
        sa.Column('wisdom', sa.Integer, nullable=False),
        sa.Column('charisma', sa.Integer, nullable=False),
        sa.Column('special', sa.String(400)),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
        )


def downgrade():
    op.drop_table('races')
