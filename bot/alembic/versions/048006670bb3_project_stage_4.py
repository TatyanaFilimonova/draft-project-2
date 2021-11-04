"""project stage 4

Revision ID: 048006670bb3
Revises: a0e9584cb9f6
Create Date: 2021-11-03 00:46:44.092512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '048006670bb3'
down_revision = 'a0e9584cb9f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('file', 'file_type',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('file', 'file_type',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###