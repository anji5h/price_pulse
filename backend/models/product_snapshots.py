from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    Boolean,
)
from datetime import datetime, timezone
from models.base import Base


class ProductSnapshot(Base):
    __tablename__ = "product_snapshots"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tracker_id: Mapped[int] = mapped_column(ForeignKey("trackers.id"), index=True)
    scrape_run_id: Mapped[int] = mapped_column(ForeignKey("scrape_runs.id"), index=True)
    title: Mapped[str] = mapped_column(String(300))
    current_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    original_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    in_stock: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    rating: Mapped[float | None] = mapped_column(Numeric(3, 2), nullable=True)
    review_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
