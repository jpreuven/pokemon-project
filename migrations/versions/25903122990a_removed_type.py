"""removed type

Revision ID: 25903122990a
Revises: 0273ddc07198
Create Date: 2023-08-07 07:55:45.164456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25903122990a'
down_revision = '0273ddc07198'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemons', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemons', sa.Column('type', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
