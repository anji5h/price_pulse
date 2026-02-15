from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Enum, Numeric
from models.base import Base
from models.enums import EventType
from datetime import datetime, timezone


class PriceEvent(Base):
    __tablename__ = "price_events"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tracker_id: Mapped[int] = mapped_column(ForeignKey("trackers.id"), index=True)
    scrape_run_id: Mapped[int] = mapped_column(ForeignKey("scrape_runs.id"), index=True)
    event_type: Mapped[EventType] = mapped_column(Enum(EventType))
    old_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    new_price: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)
    percent_change: Mapped[float | None] = mapped_column(Numeric(8, 2), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
