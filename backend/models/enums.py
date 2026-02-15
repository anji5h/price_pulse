from enum import Enum


class RoleEnum(str, Enum):
    owner = "owner"
    member = "member"


class FrequencyEnum(str, Enum):
    hourly = "hourly"
    six_hour = "6h"
    daily = "daily"


class RunStatus(str, Enum):
    pending = "pending"
    running = "running"
    success = "success"
    failed = "failed"


class EventType(str, Enum):
    price_drop = "price_drop"
    price_increase = "price_increase"
    back_in_stock = "back_in_stock"
    out_of_stock = "out_of_stock"


class Channel(str, Enum):
    email = "email"
    webhook = "webhook"
