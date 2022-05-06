"""empty message

Revision ID: 67250b3f562b
Revises: 
Create Date: 2022-05-04 17:33:26.466494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67250b3f562b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('api_key', sa.String(), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=511),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=511),
               nullable=False)
    op.drop_column('users', 'role')
    op.drop_column('users', 'api_key')
    # ### end Alembic commands ###
