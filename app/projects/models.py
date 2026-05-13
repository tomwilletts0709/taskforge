from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain import TaskStatus
from app.db import Base


class Projects(Base): 
    __tablename__: "projects"

    id: Mapped[int] = mapped_columm(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    project_id: Mapped[int] = mapped_column()
    tasks: Mapped[list["Tasks"]] = relationship(back_populates="project")
    project: Mapped["Project"] = relationship(back_populates="tasks")

    created_at: Mapped[dateime] = mapped_column(default = lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default = lambda: datetime.now(timezone.utc))

