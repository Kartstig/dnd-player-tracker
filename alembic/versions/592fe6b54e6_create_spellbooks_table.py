"""create spellbooks table

Revision ID: 592fe6b54e6
Revises: 24177dfd3f2d
Create Date: 2014-10-08 19:32:08.507298

"""

# revision identifiers, used by Alembic.
revision = '592fe6b54e6'
down_revision = '24177dfd3f2d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'spellbooks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('character_id', sa.Integer, 
            sa.ForeignKey('characters.id'), nullable=False),
        sa.Column('spell_id', sa.Integer, 
            sa.ForeignKey('spells.id'), nullable=False),
        )


def downgrade():
    op.drop_table('spellbooks')
