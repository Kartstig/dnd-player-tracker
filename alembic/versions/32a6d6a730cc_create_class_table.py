"""create class table

Revision ID: 32a6d6a730cc
Revises: 592fe6b54e6
Create Date: 2014-10-15 22:37:18.623653

"""

# revision identifiers, used by Alembic.
revision = '32a6d6a730cc'
down_revision = '592fe6b54e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('sub_class', sa.String(50)),
        sa.Column('min_str', sa.Integer, nullable=False, default=0),
        sa.Column('min_dex', sa.Integer, nullable=False, default=0),
        sa.Column('min_con', sa.Integer, nullable=False, default=0),
        sa.Column('min_int', sa.Integer, nullable=False, default=0),
        sa.Column('min_wis', sa.Integer, nullable=False, default=0),
        sa.Column('min_char', sa.Integer, nullable=False, default=0),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
        )
    op.add_column(
        'characters',
        sa.Column('class_id', sa.Integer, nullable=False)
        )
    op.create_foreign_key(
            'fk_characters_class_id_classes_id', 'characters',
            'classes', ['class_id'], ['id'])


def downgrade():
    op.drop_constraint('fk_characters_class_id_classes_id', 'characters', type_='foreignkey')
    op.drop_column('characters', 'class_id')
    op.drop_table('classes')
