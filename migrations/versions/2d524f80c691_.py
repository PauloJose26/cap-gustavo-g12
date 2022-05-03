"""empty message

Revision ID: 2d524f80c691
Revises: 12a63a1d2e96
Create Date: 2022-05-03 17:44:51.466882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2d524f80c691'
down_revision = '12a63a1d2e96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('task_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_unique_constraint(None, 'products', ['task_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='unique')
    op.drop_column('products', 'task_id')
    # ### end Alembic commands ###