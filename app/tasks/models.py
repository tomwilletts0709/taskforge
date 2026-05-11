from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    status: Mapped[str]
    created_at: Mapped[datetime.now(timezone.utc)]
    updated_at: Mapped[datetime.now(timezone.utc)]


