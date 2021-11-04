"""project stage 8

Revision ID: 73a3be186c65
Revises: 58740fb9f2e5
Create Date: 2021-11-03 16:45:23.605754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73a3be186c65'
down_revision = '58740fb9f2e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'keywords')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('keywords', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    # ### end Alembic commands ###