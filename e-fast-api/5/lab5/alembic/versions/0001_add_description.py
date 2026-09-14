from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "0001_add_description"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "documents",
        sa.Column("description", sa.String(length=250), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("documents", "description")
