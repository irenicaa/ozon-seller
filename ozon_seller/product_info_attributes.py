from dataclasses import dataclass
from typing import Iterator, Optional

from .common import credentials, request_api, make_iterative
from .common.data_class_json_mixin import DataClassJsonMixin


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


@dataclass
class GetProductAttributesPdf(DataClassJsonMixin):
    file_name: str
    name: str


@dataclass
class GetProductAttributesDictionaryValue(DataClassJsonMixin):
    dictionary_value_id: int
    value: str


@dataclass
class GetProductModelInfoValue(DataClassJsonMixin):
    model_id: int
    count: int


@dataclass
class GetProductAttributesResponseAttribute(DataClassJsonMixin):
    id: int
    complex_id: int
    values: list[GetProductAttributesDictionaryValue]


@dataclass
class GetProductAttributesResponseResult(DataClassJsonMixin):
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


@dataclass
class GetProductAttributesResponseResultWrapper(DataClassJsonMixin):
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
) -> Iterator[GetProductAttributesResponseResult]:
    return make_iterative.make_iterative_via_cursor(
        request=data,
        requester=lambda: get_product_attributes(credentials, data),
        extract_response_items=lambda response: response.result,
        cursor_attribute_name="last_id",
    )
