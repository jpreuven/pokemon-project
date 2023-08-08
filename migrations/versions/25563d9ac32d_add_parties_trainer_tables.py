"""add parties + trainer tables

Revision ID: 25563d9ac32d
Revises: d4a77c2258f9
Create Date: 2023-08-07 09:40:41.808148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25563d9ac32d'
down_revision = 'd4a77c2258f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trainers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('trainer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemons.id'], ),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parties')
    op.drop_table('trainers')
    # ### end Alembic commands ###
