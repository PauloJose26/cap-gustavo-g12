"""tables creation

Revision ID: c80ce636204d
Revises: 
Create Date: 2022-04-29 12:34:55.114508

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c80ce636204d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('country', sa.String(length=20), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('street', sa.String(length=60), nullable=False),
    sa.Column('number', sa.String(length=10), nullable=False),
    sa.Column('complement', sa.String(length=300), nullable=True),
    sa.Column('postal_code', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('description', sa.String(length=1500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partners',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cnpj', sa.String(length=14), nullable=False),
    sa.Column('phone_number', sa.String(length=12), nullable=False),
    sa.Column('about', sa.String(length=500), nullable=True),
    sa.Column('id_address', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_address'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=12), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('password_hash', sa.String(length=511), nullable=False),
    sa.Column('id_address', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_address'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('products',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('description', sa.String(length=1500), nullable=False),
    sa.Column('starting_price', sa.Numeric(), nullable=False),
    sa.Column('auction_start', sa.DateTime(), nullable=True),
    sa.Column('auction_end', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('id_partner', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['id_partner'], ['partners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bids',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('id_user', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('id_product', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_categorie',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('id_product', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('id_categorie', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['id_categorie'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_categorie')
    op.drop_table('bids')
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('partners')
    op.drop_table('categories')
    op.drop_table('addresses')
    # ### end Alembic commands ###
