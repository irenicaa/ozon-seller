from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductFilter(DataClassJsonMixin):
    offer_id: Optional[list[str]] = None
    product_id: Optional[list[str]] = None
    visibility: Optional[list[str]] = None


@dataclass
class PaginatedProductFilter(DataClassJsonMixin):
    filter: ProductFilter
    last_id: str
    limit: int
    sort_by: str
    sort_dit: str


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesPdf:
    file_name: str
    index: int
    name: str

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesImage360:
    file_name: str
    index: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesImage:
    default: bool
    file_name: str
    index: int



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesDictionaryValue:
    dictionary_value_id: int
    value: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesResponseAttribute:
    attribute_id: int
    complex_id: int
    values: list[GetProductAttributesDictionaryValue]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesResponseResult:
    attributes: list[GetProductAttributesResponseAttribute]
    barcode: str
    category_id: int
    color_image: str
    complex_attributes: list[GetProductAttributesResponseAttribute]
    depth: int
    dimension_unit: str
    height: int
    id: int
    image_group_id: str
    images: list[GetProductAttributesImage]
    images360: list[GetProductAttributesImage360]
    name: str
    offer_id: str
    pdf_list: list[GetProductAttributesPdf]
    weight: int
    weight_unit: str
    width: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesResponseResultWrapper:
    result: list[GetProductAttributesResponseResult]
    last_id: str
    total: int

def get_product_attributes(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> GetProductAttributesResponseResultWrapper:
    return request_api.request_api_json(
        "POST",
        "/v3/products/info/attributes",
        credentials,
        data,
        response_cls=GetProductAttributesResponseResultWrapper,
    )


def get_product_attributes_iterative(
    credentials: credentials.Credentials,
    data: PaginatedProductFilter,
) -> Generator[GetProductAttributesResponseResultWrapper, None, None]:
    while True:
        attributes = get_product_attributes(credentials, data)
        if attributes.result == []:
            break

        yield attributes

        data.last_id = attributes.last_id
