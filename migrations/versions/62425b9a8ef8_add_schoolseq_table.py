"""add SchoolSeq  table

Revision ID: 62425b9a8ef8
Revises: e58fe869dcfd
Create Date: 2019-11-17 01:53:57.737373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62425b9a8ef8'
down_revision = 'e58fe869dcfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schoolseqs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seqdatatime', sa.DateTime(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.Column('classnum', sa.Integer(), nullable=True),
    sa.Column('studentnum', sa.Integer(), nullable=True),
    sa.Column('venuenum', sa.Integer(), nullable=True),
    sa.Column('teachernum', sa.Integer(), nullable=True),
    sa.Column('workernum', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schoolseqs_seqdatatime'), 'schoolseqs', ['seqdatatime'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_schoolseqs_seqdatatime'), table_name='schoolseqs')
    op.drop_table('schoolseqs')
    # ### end Alembic commands ###
