"""columns add

Revision ID: ac868e765646
Revises: 
Create Date: 2022-08-05 08:41:05.024071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac868e765646'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("password", "hased_password", nullable=True)
    op.add_column("users", sa.Column("verify_code", sa.String))
    pass


def downgrade() -> None:
    pass
