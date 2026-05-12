from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column

from app.domain import TaskStatus, Roles
from app.db import Base


class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)

    role: Mapped[str] = mapped_column(default=Roles.MEMBER.value)

    created_at: Mapped[datetime] = mapped_column(default= lambda: datetime.now(timezone.utc))
    
