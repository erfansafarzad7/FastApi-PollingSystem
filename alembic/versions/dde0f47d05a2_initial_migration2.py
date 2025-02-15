"""initial migration2

Revision ID: dde0f47d05a2
Revises: 95fa50ec14c4
Create Date: 2025-01-06 16:22:36.709597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dde0f47d05a2'
down_revision: Union[str, None] = '95fa50ec14c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('polls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_polls_id'), 'polls', ['id'], unique=False)
    op.create_index(op.f('ix_polls_question'), 'polls', ['question'], unique=False)
    op.create_table('options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('poll_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['poll_id'], ['polls.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_options_id'), 'options', ['id'], unique=False)
    op.create_index(op.f('ix_options_text'), 'options', ['text'], unique=False)
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poll_id', sa.Integer(), nullable=True),
    sa.Column('option_id', sa.Integer(), nullable=True),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['option_id'], ['options.id'], ),
    sa.ForeignKeyConstraint(['poll_id'], ['polls.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_votes_id'), 'votes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_votes_id'), table_name='votes')
    op.drop_table('votes')
    op.drop_index(op.f('ix_options_text'), table_name='options')
    op.drop_index(op.f('ix_options_id'), table_name='options')
    op.drop_table('options')
    op.drop_index(op.f('ix_polls_question'), table_name='polls')
    op.drop_index(op.f('ix_polls_id'), table_name='polls')
    op.drop_table('polls')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
