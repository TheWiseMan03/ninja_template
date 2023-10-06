from typing import Any
from ninja import Schema


class BasePaginatedResponseSchema(Schema):
    """To use this schema you need to provide items key"""

    items: Any
    total: int
    page: int
    size: int
