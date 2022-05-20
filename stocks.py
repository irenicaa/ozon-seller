from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ProductFilter:
    offer_id: List[str]
    product_id: List[str]
    visibility: str

@dataclass_json
@dataclass
class PaginatedProductFilter:
    filter: ProductFilter
    last_id: str
    limit: int
