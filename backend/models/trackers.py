from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Enum,
    Numeric,
    Boolean,
    UniqueConstraint,
)
from datetime import datetime, timezone
from models.base import Base
from models.enums import FrequencyEnum


class Tracker(Base):
    __tablename__ = "trackers"
    __table_args__ = (
        UniqueConstraint("project_id", "competitor_url", name="uq_tracker_url_project"),
    )
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), index=True)
    name: Mapped[str] = mapped_column(String(180))
    competitor_url: Mapped[str] = mapped_column(String(1024))
    site_name: Mapped[str] = mapped_column(String(120))
    currency: Mapped[str] = mapped_column(String(10), default="USD")
    own_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    target_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    scrape_frequency: Mapped[FrequencyEnum] = mapped_column(
        Enum(FrequencyEnum), default=FrequencyEnum.daily
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    project = relationship("Project", back_populates="trackers")
