"""empty message

Revision ID: de877fd3d0d7
Revises: 637672972f10
Create Date: 2021-08-18 11:09:07.921099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de877fd3d0d7'
down_revision = '637672972f10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('pronouns', sa.String(length=250), nullable=True))
    op.add_column('user', sa.Column('grad_year', sa.String(length=250), nullable=True))
    op.add_column('user', sa.Column('classes', sa.String(length=250), nullable=False))
    op.add_column('user', sa.Column('pref_time', sa.String(length=250), nullable=True))
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'last_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.drop_column('user', 'pref_time')
    op.drop_column('user', 'classes')
    op.drop_column('user', 'grad_year')
    op.drop_column('user', 'pronouns')
    # ### end Alembic commands ###
