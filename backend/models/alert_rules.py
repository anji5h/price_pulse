from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric, Boolean
from models.base import Base


class AlertRule(Base):
    __tablename__ = "alert_rules"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), unique=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    percent_drop_threshold: Mapped[float | None] = mapped_column(
        Numeric(8, 2), nullable=True
    )
    absolute_price_threshold: Mapped[float | None] = mapped_column(
        Numeric(12, 2), nullable=True
    )
    webhook_url: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    email_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
