from dataclasses import dataclass
from typing import Union, Callable, Any, Optional
import datetime
import unittest
import pathlib

from . import common
from .test_server_endpoint import TestServerEndpoint
from .test_server import TestServer
from ..common import data_class_json_mixin
from ..common import credentials
from ..common import request_api
from .. import (
    actions_candidates,
    actions_products,
    actions,
    chat_send_message,
    chat_start,
    fbs_act_get_postings,
    posting_fbo_list,
    posting_fbs_act_check_status,
    posting_fbs_act_create,
    posting_fbs_act_get_barcode,
    posting_fbs_get,
    posting_fbs_list,
    posting_fbs_package_label,
    posting_fbs_product_country_list,
    posting_fbs_product_country_set,
    posting_fbs_ship_gtd,
    product_description,
    product_import_prices,
    product_import_stocks,
    product_info_attributes,
    product_info,
    product_pictures_import,
    products_stocks,
    returns_fbo,
    returns_fbs,
    stocks,
)


@dataclass
class _IntegrationTestCase: # type: ignore[misc]
    kind: str
    requester: Union[
        Callable[[credentials.Credentials, Any], Any],
        Callable[[credentials.Credentials], Any],
    ]
    request_credentials: credentials.Credentials
    request_data: Optional[data_class_json_mixin.DataClassJsonMixin]
    expected_method: str
    expected_endpoint: str
    response_cls: Optional[type[data_class_json_mixin.DataClassJsonMixin]]


_TEST_DATA_PATH = pathlib.Path(__file__).parent.joinpath(common.TEST_DATA_DIRECTORY)
_TEST_EXPECTED_CREDENTIALS = credentials.Credentials(client_id="client-id", api_key="api-key")
_TEST_TEXT_RESPONSE_DATA = "text-response-data"
_INTEGRATION_TEST_CASES: list[_IntegrationTestCase] = [
    # actions_candidates
    _IntegrationTestCase(
        kind="success",
        requester=actions_candidates.get_actions_candidates,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=actions_candidates.PaginatedCandidatesForActions(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/candidates",
        response_cls=actions_candidates.GetActionsCandidatesResponseResultWrapper,
    ),

    # actions_products
    _IntegrationTestCase(
        kind="success",
        requester=actions_products.get_action_products,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=actions_products.PaginatedActionProducts(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/products",
        response_cls=actions_products.GetSellerProductResponseResultWrapper,
    ),

    # actions
    _IntegrationTestCase(
        kind="success",
        requester=actions.get_actions,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=None,
        expected_method="GET",
        expected_endpoint="/v1/actions",
        response_cls=actions.GetSellerActionsResponseResultWrapper,
    ),

    # chat_send_message
    _IntegrationTestCase(
        kind="success",
        requester=chat_send_message.send_message,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=chat_send_message.ChatMessageData(
            chat_id="23",
            text="test",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/send/message",
        response_cls=chat_send_message.GetChatStartResponseResult,
    ),

    # chat_start
    _IntegrationTestCase(
        kind="success",
        requester=chat_start.get_chat_id,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=chat_start.ChatStartData(
            posting_number="23",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/start",
        response_cls=chat_start.GetChatStartResponseResultWrapper,
    ),

    # fbs_act_get_postings
    _IntegrationTestCase(
        kind="success",
        requester=fbs_act_get_postings.get_posting_fbs_act_data,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=fbs_act_get_postings.PostingFBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-postings",
        response_cls=fbs_act_get_postings.PostingFBSActDataResponseResultWrapper,
    ),

    # posting_fbo_list
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbo_list.get_posting_fbo_list,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbo_list.PaginatedGetPostingFBOListFilter(
            filter=posting_fbo_list.GetPostingFBOListFilter(
                since=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
                status="status",
            ),
            dir="DESC",
            translit=True,
            limit=23,
            offset=42,
            with_=posting_fbo_list.PostingAdditionalFields(
                analytics_data=True,
                financial_data=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbo/list",
        response_cls=posting_fbo_list.GetPostingFBOListResponseResultWrapper,
    ),

    # posting_fbs_act_check_status
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_check_status.create_posting_fbs_act,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_act_check_status.PostingFSBActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/check-status",
        response_cls=posting_fbs_act_check_status.PostingFBSActCreateResponseActResultWrapper,
    ),

    # posting_fbs_act_create
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_create.create_posting_fbs_act,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_act_create.PostingFSBDeliveryData(
            containers_count=23,
            delivery_method_id=42,
            departure_date=datetime.datetime.fromisoformat(
                "2006-01-02T15:04:05.999999+07:00",
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/create",
        response_cls=posting_fbs_act_create.PostingFBSActCreateResponseActResultWrapper,
    ),

    # posting_fbs_act_get_barcode
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_get_barcode.get_posting_fbs_act_barcode,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_act_get_barcode.FBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-barcode",
        response_cls=None,
    ),

    # posting_fbs_get
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_get.get_posting_fbs_data,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_get.PostingFBSData(
            posting_number="23",
            with_=posting_fbs_get.PostingAdditionalFields(
                analytics_data=True,
                barcodes=True,
                financial_data=True,
                translit=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v3/posting/fbs/get",
        response_cls=posting_fbs_get.GetPostingFBSDataResponseResultWrapper,
    ),

    # posting_fbs_list
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
            filter=posting_fbs_list.GetPostingFBSListFilter(
                delivery_method_id=[123, 142],
                order_id=12,
                provider_id=[223, 242],
                status="status",
                warehouse_id=[323, 342],
                since=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
            ),
            dir="DESC",
            limit=23,
            offset=42,
            with_=posting_fbs_list.PostingAdditionalFields(
                analytics_data=True,
                barcodes=True,
                financial_data=True,
                translit=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v3/posting/fbs/list",
        response_cls=posting_fbs_list.GetPostingFBSListResponseResultWrapper,
    ),

    # posting_fbs_package_label
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_package_label.get_posting_fbs_package_label,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_package_label.FBSPackageData(
            posting_number=["23", "42"],
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/package-label",
        response_cls=None,
    ),

    # posting_fbs_list
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
            filter=posting_fbs_list.GetPostingFBSListFilter(
                delivery_method_id=[123, 142],
                order_id=12,
                provider_id=[223, 242],
                status="status",
                warehouse_id=[323, 342],
                since=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
            ),
            dir="DESC",
            limit=23,
            offset=42,
            with_=posting_fbs_list.PostingAdditionalFields(
                analytics_data=True,
                barcodes=True,
                financial_data=True,
                translit=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v3/posting/fbs/list",
        response_cls=posting_fbs_list.GetPostingFBSListResponseResultWrapper,
    ),

    # posting_fbs_product_country_list
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_product_country_list.get_posting_fbs_product_country_list,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_product_country_list.CountryFilter(
            name_search="name",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/list",
        response_cls=posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResultWrapper,
    ),

    # posting_fbs_product_country_set
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_product_country_set.posting_fbs_product_country_set,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_product_country_set.OderData(
            posting_number="23",
            product_id=42,
            country_iso_code="US",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/set",
        response_cls=posting_fbs_product_country_set.GetCountrySetFBSResponseResult,
    ),

    # posting_fbs_ship_gtd
    _IntegrationTestCase(
        kind="success",
        requester=posting_fbs_ship_gtd.create_posting_fbs_ship_with_gtd,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-105",
                                    gtd="gtd-105",
                                    is_gtd_absent=False,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-112",
                                    gtd="gtd-112",
                                    is_gtd_absent=False,
                                ),
                            ],
                            product_id=123,
                            quantity=142,
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-205",
                                    gtd="gtd-205",
                                    is_gtd_absent=False,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-212",
                                    gtd="gtd-212",
                                    is_gtd_absent=False,
                                ),
                            ],
                            product_id=223,
                            quantity=242,
                        ),
                    ],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-305",
                                    gtd="gtd-305",
                                    is_gtd_absent=False,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-312",
                                    gtd="gtd-312",
                                    is_gtd_absent=False,
                                ),
                            ],
                            product_id=323,
                            quantity=342,
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-405",
                                    gtd="gtd-405",
                                    is_gtd_absent=False,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    mandatory_mark="mandatory-mark-412",
                                    gtd="gtd-412",
                                    is_gtd_absent=False,
                                ),
                            ],
                            product_id=423,
                            quantity=442,
                        ),
                    ],
                ),
            ],
            posting_number="500",
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(
                additional_data=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v3/posting/fbs/ship",
        response_cls=posting_fbs_ship_gtd.CreatePostingFBSShipWithGTDResponseResultWrapper,
    ),

    # product_description
    _IntegrationTestCase(
        kind="success",
        requester=product_description.get_product_description,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_description.ProductData(
            offer_id="23",
            product_id=42,
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/info/description",
        response_cls=product_description.GetProductInfoDescriptionResponseResultWrapper,
    ),

    # product_import_prices
    _IntegrationTestCase(
        kind="success",
        requester=product_import_prices.set_product_import_price,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_import_prices.PricesData(
            prices=[
                product_import_prices.ItemPriceData(
                    auto_action_enabled="one",
                    min_price="1.5",
                    offer_id="112",
                    old_price="1.23",
                    price="1.42",
                    product_id=100,
                ),
                product_import_prices.ItemPriceData(
                    auto_action_enabled="two",
                    min_price="2.5",
                    offer_id="212",
                    old_price="2.23",
                    price="2.42",
                    product_id=200,
                ),
            ],
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/import/prices",
        response_cls=product_import_prices.GetProductImportPriceResponseResultWrapper,
    ),

    # product_import_stocks
    _IntegrationTestCase(
        kind="success",
        requester=product_import_stocks.set_stocks,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_import_stocks.ProductImportProductsStocks(
            stocks=[
                product_import_stocks.ProductsStocksList(
                    offer_id="1.5",
                    product_id=112,
                    stock=123,
                    warehouse_id=142,
                ),
                product_import_stocks.ProductsStocksList(
                    offer_id="2.5",
                    product_id=212,
                    stock=223,
                    warehouse_id=242,
                ),
            ],
        ),
        expected_method="POST",
        expected_endpoint="/v2/products/stocks",
        response_cls=product_import_stocks.ProductsStocksResponseProcessResultWrapper,
    ),

    # product_info_attributes
    _IntegrationTestCase(
        kind="success",
        requester=product_info_attributes.get_product_attributes,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(
                offer_id=["105", "205"],
                product_id=["112", "212"],
                sku=["123", "223"],
                visibility=["one", "two"],
            ),
            last_id="23",
            limit=42,
            sort_dir="sort-dir",
            sort_by="sort-by",
        ),
        expected_method="POST",
        expected_endpoint="/v4/product/info/attributes",
        response_cls=product_info_attributes.GetProductAttributesResponseResultWrapper,
    ),

    # product_info
    _IntegrationTestCase(
        kind="success",
        requester=product_info.get_product_info,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_info.ProductData(
            offer_id="12",
            product_id=23,
            sku=42,
        ),
        expected_method="POST",
        expected_endpoint="/v2/product/info",
        response_cls=product_info.GetProductInfoResponseResultWrapper,
    ),

    # product_pictures_import
    _IntegrationTestCase(
        kind="success",
        requester=product_pictures_import.send_product_pictures,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=product_pictures_import.ProductPictures(
            color_image="color image",
            images=["image #1", "image #2"],
            images360=["images 360 #1", "images 360 #2"],
            product_id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/pictures/import",
        response_cls=product_pictures_import.ProductPicturesResponseResultWrapper,
    ),

    # products_stocks
    _IntegrationTestCase(
        kind="success",
        requester=products_stocks.set_stocks,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=products_stocks.StocksData(
            stocks=[
                products_stocks.ProductData(
                    offer_id="1.5",
                    product_id=112,
                    stock=123,
                    warehouse_id=142,
                ),
                products_stocks.ProductData(
                    offer_id="2.5",
                    product_id=212,
                    stock=223,
                    warehouse_id=242,
                ),
            ],
        ),
        expected_method="POST",
        expected_endpoint="/v2/products/stocks",
        response_cls=products_stocks.SetProductStocksResponseResultWrapper,
    ),

    # returns_fbo
    _IntegrationTestCase(
        kind="success",
        requester=returns_fbo.get_returns_company_fbo,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(
            filter=returns_fbo.GetReturnsCompanyFBOFilter(
                posting_number="12",
                status=["one", "two"],
            ),
            offset=23,
            limit=42,
        ),
        expected_method="POST",
        expected_endpoint="/v2/returns/company/fbo",
        response_cls=returns_fbo.GetReturnsCompanyFBOResponseResult,
    ),

    # returns_fbs
    _IntegrationTestCase(
        kind="success",
        requester=returns_fbs.get_returns_company_fbs,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=returns_fbs.PaginatedGetReturnsCompanyFBSFilter(
            filter=returns_fbs.GetReturnsCompanyFBSFilter(
                accepted_from_customer_moment=[
                    returns_fbs.FilterTimeRange(
                        time_from=datetime.datetime.fromisoformat(
                            "2006-01-02T15:04:05.999999+07:00",
                        ),
                        time_to=datetime.datetime.fromisoformat(
                            "2006-01-02T17:04:05.999999+07:00",
                        ),
                    ),
                    returns_fbs.FilterTimeRange(
                        time_from=datetime.datetime.fromisoformat(
                            "2006-01-03T15:04:05.999999+07:00",
                        ),
                        time_to=datetime.datetime.fromisoformat(
                            "2006-01-03T17:04:05.999999+07:00",
                        ),
                    ),
                ],
                last_free_waiting_day=[
                    returns_fbs.FilterTimeRange(
                        time_from=datetime.datetime.fromisoformat(
                            "2006-01-04T15:04:05.999999+07:00",
                        ),
                        time_to=datetime.datetime.fromisoformat(
                            "2006-01-04T17:04:05.999999+07:00",
                        ),
                    ),
                    returns_fbs.FilterTimeRange(
                        time_from=datetime.datetime.fromisoformat(
                            "2006-01-05T15:04:05.999999+07:00",
                        ),
                        time_to=datetime.datetime.fromisoformat(
                            "2006-01-05T17:04:05.999999+07:00",
                        ),
                    ),
                ],
                order_id=5,
                posting_number=["123", "142"],
                product_name="product_name",
                product_offer_id="12",
                status="status",
            ),
            offset=23,
            limit=42,
        ),
        expected_method="POST",
        expected_endpoint="/v2/returns/company/fbs",
        response_cls=returns_fbs.GetReturnsCompanyFBSResponseResultWrapper,
    ),

    # stocks
    _IntegrationTestCase(
        kind="success",
        requester=stocks.get_product_info_stocks,
        request_credentials=_TEST_EXPECTED_CREDENTIALS,
        request_data=stocks.PaginatedProductFilter(
            filter=stocks.ProductFilter(
                offer_id=["105", "205"],
                product_id=["112", "212"],
                visibility="visibility",
                with_quant=stocks.ProductFilterWithQuant(
                    created=True,
                ),
            ),
            cursor="23",
            limit=42,
        ),
        expected_method="POST",
        expected_endpoint="/v4/product/info/stocks",
        response_cls=stocks.GetProductInfoStocksResponseResult,
    ),
]


class TestIntegration(unittest.TestCase):
    def test_integration(self) -> None:
        for test_case in _INTEGRATION_TEST_CASES:
            requester_name = common.get_last_module(test_case.requester)
            test_case_name = f"{requester_name} [{test_case.kind}]"

            with self.subTest(test_case_name):
                request_module = common.get_last_module(test_case.request_data) \
                    if test_case.request_data is not None \
                    else None
                response_module = common.get_last_module(test_case.response_cls) \
                    if test_case.response_cls is not None \
                    else None
                if (
                    request_module is not None
                    and response_module is not None
                    and request_module != response_module
                ):
                    raise RuntimeError(
                        "different modules for the request and response: " +
                            f"{request_module} and {response_module}, respectively",
                    )

                expected_request_json = None
                if test_case.request_data is not None:
                    expected_request_json_filename = "full.json"
                    expected_request_json_path = _TEST_DATA_PATH.joinpath(
                        common.get_last_module(test_case.request_data),
                        common.get_qualified_name(test_case.request_data),
                        expected_request_json_filename,
                    )

                    with open(expected_request_json_path) as expected_request_json_file:
                        expected_request_json = expected_request_json_file.read().strip()

                expected_response: Any
                if test_case.response_cls is not None:
                    response_type = "application/json"

                    response_json_filename = "full.json"
                    response_json_path = _TEST_DATA_PATH.joinpath(
                        common.get_last_module(test_case.response_cls),
                        common.get_qualified_name(test_case.response_cls),
                        response_json_filename,
                    )

                    with open(response_json_path) as response_json_file:
                        response_data = response_json_file.read().strip()

                    expected_response = test_case.response_cls.schema().loads(response_data)
                else:
                    response_type = "text/plain"
                    response_data = _TEST_TEXT_RESPONSE_DATA
                    expected_response = _TEST_TEXT_RESPONSE_DATA.encode("utf-8")

                with TestServer(TestServerEndpoint(
                    expected_method=test_case.expected_method,
                    expected_endpoint=test_case.expected_endpoint,
                    expected_credentials=_TEST_EXPECTED_CREDENTIALS,
                    expected_request_json=expected_request_json,
                    provided_response_type=response_type,
                    provided_response_data=response_data,
                )) as server:
                    request_api._API_BASE_URL = server.address

                    requester_args = (test_case.request_credentials, test_case.request_data) \
                        if test_case.request_data is not None \
                        else (test_case.request_credentials,)
                    actual_response = test_case.requester(*requester_args) # type: ignore[arg-type]

                    self.assertEqual(expected_response, actual_response)
