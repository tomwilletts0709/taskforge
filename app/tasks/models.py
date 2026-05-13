from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column, ForeignKey

from app.domain import TaskStatus
from app.db import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), index=True)
    description: Mapped[str | None] = mapped_column(default=None)
    status: Mapped[str] = mapped_column(default=TaskStatus.TODO.value)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

