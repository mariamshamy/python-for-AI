from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0002_add_ai_summary"
down_revision: Union[str, None] = "0001_add_description"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "documents",
        sa.Column(
            "ai_summary",
            sa.Text(),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("documents", "ai_summary")
