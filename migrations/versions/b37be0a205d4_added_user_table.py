"""Added user table

Revision ID: b37be0a205d4
Revises: c609270e720d
Create Date: 2019-11-13 16:41:18.112039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b37be0a205d4'
down_revision = 'c609270e720d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('github_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('ix_users_github_id'), 'users', ['github_id'], unique=False)
    op.create_index(op.f('ix_users_is_admin'), 'users', ['is_admin'], unique=False)
    op.create_index(op.f('ix_users_last_login'), 'users', ['last_login'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_last_login'), table_name='users')
    op.drop_index(op.f('ix_users_is_admin'), table_name='users')
    op.drop_index(op.f('ix_users_github_id'), table_name='users')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
