"""empty message

Revision ID: 3fc5498303f1
Revises: 
Create Date: 2019-08-22 21:09:00.295978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc5498303f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('import',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('citizen_id', sa.Integer(), nullable=False),
    sa.Column('import_id', sa.Integer(), nullable=False),
    sa.Column('town', sa.String(length=256), nullable=False),
    sa.Column('street', sa.String(length=256), nullable=False),
    sa.Column('building', sa.String(length=256), nullable=False),
    sa.Column('apartment', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('birth_date', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('relatives', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['import_id'], ['import.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('import')
    # ### end Alembic commands ###
