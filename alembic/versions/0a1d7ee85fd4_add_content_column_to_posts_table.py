"""add content column to posts table

Revision ID: 0a1d7ee85fd4
Revises: a3de7a12d10c
Create Date: 2022-04-09 09:23:30.224884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a1d7ee85fd4'
down_revision = 'a3de7a12d10c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
