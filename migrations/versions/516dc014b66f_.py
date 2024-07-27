"""empty message

Revision ID: 516dc014b66f
Revises: 2ce59ebcc0b3
Create Date: 2024-07-26 23:13:35.113396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '516dc014b66f'
down_revision = '2ce59ebcc0b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('character_films')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character_films',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('film_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], name='character_films_character_id_fkey'),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], name='character_films_film_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='character_films_pkey')
    )
    op.drop_table('favorite_character')
    # ### end Alembic commands ###