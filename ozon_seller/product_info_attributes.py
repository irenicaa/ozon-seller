from dataclasses import dataclass
from typing import Generator, Optional

from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from .common import credentials, request_api

# Request


@dataclass
class ProductFilter(DataClassJsonMixin):
    offer_id: Optional[list[str]] = None
    product_id: Optional[list[str]] = None
    sku: Optional[list[str]] = None
    visibility: Optional[list[str]] = None


@dataclass
class PaginatedProductFilter(DataClassJsonMixin):
    filter: ProductFilter
    last_id: str
    limit: int
    sort_dir: Optional[str]
    sort_by: Optional[str] = ""


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesPdf:
    file_name: str
    name: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesImage360:
    file_name: str
    index: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesDictionaryValue:
    dictionary_value_id: int
    value: str


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductModelInfoValue:
    model_id: int
    count: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesResponseAttribute:
    id: int
    complex_id: int
    values: list[GetProductAttributesDictionaryValue]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetProductAttributesResponseResult:
    attributes: list[GetProductAttributesResponseAttribute]
    barcode: str
    barcodes: list[str]
    description_category_id: int
    color_image: str
    complex_attributes: list[GetProductAttributesResponseAttribute]
    depth: int
    dimension_unit: str
    height: int
    id: int
    images: list[str]
    model_info: GetProductModelInfoValue
    name: str
    offer_id: str
    pdf_list: list[GetProductAttributesPdf]
    primary_image: str
    sku: int
    type_id: int
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
        "/v4/product/info/attributes",
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
