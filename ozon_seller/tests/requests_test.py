from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
import datetime
import unittest
import pathlib

from . import common
from .. import (
    actions_candidates,
    actions_products,
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
class _RequestsTestCase:
    kind: str
    data: DataClassJsonMixin


_TEST_DATA_PATH = pathlib.Path(__file__).parent.joinpath(common.TEST_DATA_DIRECTORY)
_REQUESTS_TEST_CASES: list[_RequestsTestCase] = [
    # actions_candidates.PaginatedCandidatesForActions
    _RequestsTestCase(
        kind="empty",
        data=actions_candidates.PaginatedCandidatesForActions(),
    ),
    _RequestsTestCase(
        kind="full",
        data=actions_candidates.PaginatedCandidatesForActions(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
    ),

    # actions_products.PaginatedActionProducts
    _RequestsTestCase(
        kind="empty",
        data=actions_products.PaginatedActionProducts(),
    ),
    _RequestsTestCase(
        kind="full",
        data=actions_products.PaginatedActionProducts(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
    ),

    # chat_send_message.ChatMessageData
    _RequestsTestCase(
        kind="empty",
        data=chat_send_message.ChatMessageData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=chat_send_message.ChatMessageData(
            chat_id="23",
            text="test",
        ),
    ),

    # chat_start.ChatStartData
    _RequestsTestCase(
        kind="empty",
        data=chat_start.ChatStartData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=chat_start.ChatStartData(
            posting_number="23",
        ),
    ),

    # fbs_act_get_postings.PostingFBSActData
    _RequestsTestCase(
        kind="empty",
        data=fbs_act_get_postings.PostingFBSActData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=fbs_act_get_postings.PostingFBSActData(
            id=23,
        ),
    ),

    # posting_fbo_list.PaginatedGetPostingFBOListFilter
    _RequestsTestCase(
        kind="top_level_empty",
        data=posting_fbo_list.PaginatedGetPostingFBOListFilter(),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=posting_fbo_list.PaginatedGetPostingFBOListFilter(
            filter=posting_fbo_list.GetPostingFBOListFilter(),
            with_=posting_fbo_list.PostingAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="nulls",
        data=posting_fbo_list.PaginatedGetPostingFBOListFilter(
            filter=posting_fbo_list.GetPostingFBOListFilter(),
            dir=None,
            translit=None,
            with_=posting_fbo_list.PostingAdditionalFields(
                analytics_data=None,
                financial_data=None,
            ),
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbo_list.PaginatedGetPostingFBOListFilter(
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
    ),

    # posting_fbs_act_check_status.PostingFSBActData
    _RequestsTestCase(
        kind="empty",
        data=posting_fbs_act_check_status.PostingFSBActData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_act_check_status.PostingFSBActData(
            id=23,
        ),
    ),

    # posting_fbs_act_create.PostingFSBDeliveryData
    _RequestsTestCase(
        kind="empty",
        data=posting_fbs_act_create.PostingFSBDeliveryData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_act_create.PostingFSBDeliveryData(
            containers_count=23,
            delivery_method_id=42,
            departure_date=datetime.datetime.fromisoformat(
                "2006-01-02T15:04:05.999999+07:00",
            ),
        ),
    ),

    # posting_fbs_act_get_barcode.FBSActData
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_act_get_barcode.FBSActData(
            id=23,
        ),
    ),

    # posting_fbs_get.PostingFBSData
    _RequestsTestCase(
        kind="minimal",
        data=posting_fbs_get.PostingFBSData(
            posting_number="23",
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=posting_fbs_get.PostingFBSData(
            posting_number="23",
            with_=posting_fbs_get.PostingAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_get.PostingFBSData(
            posting_number="23",
            with_=posting_fbs_get.PostingAdditionalFields(
                analytics_data=True,
                barcodes=True,
                financial_data=True,
                translit=True,
            ),
        ),
    ),

    # posting_fbs_list.PaginatedGetPostingFBSListFilter
    _RequestsTestCase(
        kind="top_level_empty",
        data=posting_fbs_list.PaginatedGetPostingFBSListFilter(),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
            filter=posting_fbs_list.GetPostingFBSListFilter(),
            with_=posting_fbs_list.PostingAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_lists",
        data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
            filter=posting_fbs_list.GetPostingFBSListFilter(
                delivery_method_id=[],
                provider_id=[],
                warehouse_id=[],
            ),
            with_=posting_fbs_list.PostingAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="nulls",
        data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
            filter=posting_fbs_list.GetPostingFBSListFilter(),
            dir=None,
            with_=posting_fbs_list.PostingAdditionalFields(
                analytics_data=None,
                barcodes=None,
                financial_data=None,
                translit=None,
            ),
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_list.PaginatedGetPostingFBSListFilter(
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
    ),

    # posting_fbs_package_label.FBSPackageData
    _RequestsTestCase(
        kind="empty_list",
        data=posting_fbs_package_label.FBSPackageData(
            posting_number=[],
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_package_label.FBSPackageData(
            posting_number=["23", "42"],
        ),
    ),

    # posting_fbs_product_country_list.CountryFilter
    _RequestsTestCase(
        kind="empty",
        data=posting_fbs_product_country_list.CountryFilter(),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_product_country_list.CountryFilter(
            name_search="name",
        ),
    ),

    # posting_fbs_product_country_set.OderData
    _RequestsTestCase(
        kind="nulls",
        data=posting_fbs_product_country_set.OderData(
            posting_number=None,
            product_id=None,
            country_iso_code=None,
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_product_country_set.OderData(
            posting_number="23",
            product_id=42,
            country_iso_code="US",
        ),
    ),

    # posting_fbs_ship_gtd.PostingFBSShipWithGTDData
    _RequestsTestCase(
        kind="top_level_empty",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(),
    ),
    _RequestsTestCase(
        kind="top_level_empty_list",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[],
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_list",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[],
                ),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="third_level_empty",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(),
                    ],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(),
                    ],
                ),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="third_level_empty_list",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[],
                        ),
                    ],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[],
                        ),
                    ],
                ),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="fourth_level_empty",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                            ],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                            ],
                        ),
                    ],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                            ],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(),
                            ],
                        ),
                    ],
                ),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(),
        ),
    ),
    _RequestsTestCase(
        kind="nulls",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
            packages=[
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                            ],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                            ],
                        ),
                    ],
                ),
                posting_fbs_ship_gtd.PostingFBSShipWithGTDPackage(
                    products=[
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                            ],
                        ),
                        posting_fbs_ship_gtd.PostingFBSShipWithGTDProduct(
                            exemplar_info=[
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                                posting_fbs_ship_gtd.PostingFBSShipWithGTDExemplarInfo(
                                    is_gtd_absent=None,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
            with_=posting_fbs_ship_gtd.PostingFBSShipWithGTDAdditionalFields(
                additional_data=None,
            ),
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=posting_fbs_ship_gtd.PostingFBSShipWithGTDData(
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
    ),

    # product_description.ProductData
    _RequestsTestCase(
        kind="empty",
        data=product_description.ProductData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_description.ProductData(
            offer_id="23",
            product_id=42,
        ),
    ),

    # product_import_prices.PricesData
    _RequestsTestCase(
        kind="empty",
        data=product_import_prices.PricesData(),
    ),
    _RequestsTestCase(
        kind="empty_list",
        data=product_import_prices.PricesData(
            prices=[],
        ),
    ),
    _RequestsTestCase(
        kind="empty_item",
        data=product_import_prices.PricesData(
            prices=[
                product_import_prices.ItemPriceData(),
            ],
        ),
    ),
    _RequestsTestCase(
        kind="item_with_nulls",
        data=product_import_prices.PricesData(
            prices=[
                product_import_prices.ItemPriceData(
                    auto_action_enabled=None,
                ),
            ],
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_import_prices.PricesData(
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
    ),

    # product_import_stocks.ProductImportProductsStocks
    _RequestsTestCase(
        kind="second_level_empty_lists",
        data=product_import_stocks.ProductImportProductsStocks(
            stocks=[],
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_import_stocks.ProductImportProductsStocks(
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
    ),

    # product_info_attributes.PaginatedProductFilter
    _RequestsTestCase(
        kind="minimal",
        data=product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(),
            last_id="23",
            limit=42,
            sort_dir=None,
            sort_by=None,
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(),
            last_id="23",
            limit=42,
            sort_dir="sort-dir",
            sort_by="sort-by",
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_lists",
        data=product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(
                offer_id=[],
                product_id=[],
                sku=[],
                visibility=[],
            ),
            last_id="23",
            limit=42,
            sort_dir="sort-dir",
            sort_by="sort-by",
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_info_attributes.PaginatedProductFilter(
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
    ),

    # product_info.ProductData
    _RequestsTestCase(
        kind="empty",
        data=product_info.ProductData(),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_info.ProductData(
            offer_id="12",
            product_id=23,
            sku=42,
        ),
    ),

    # product_pictures_import.ProductPictures
    _RequestsTestCase(
        kind="empty",
        data=product_pictures_import.ProductPictures(),
    ),
    _RequestsTestCase(
        kind="empty_list",
        data=product_pictures_import.ProductPictures(
            color_image="color image",
            images=[],
            images360=[],
            product_id=23,
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=product_pictures_import.ProductPictures(
            color_image="color image",
            images=["image #1", "image #2"],
            images360=["images 360 #1", "images 360 #2"],
            product_id=23,
        ),
    ),

    # products_stocks.StocksData
    _RequestsTestCase(
        kind="empty",
        data=products_stocks.StocksData(),
    ),
    _RequestsTestCase(
        kind="empty_list",
        data=products_stocks.StocksData(
            stocks=[],
        ),
    ),
    _RequestsTestCase(
        kind="empty_item",
        data=products_stocks.StocksData(
            stocks=[
                products_stocks.ProductData(),
            ],
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=products_stocks.StocksData(
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
    ),

    # returns_fbo.PaginatedGetReturnsCompanyFBOFilter
    _RequestsTestCase(
        kind="top_level_empty",
        data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(),
    ),
    _RequestsTestCase(
        kind="second_level_empty",
        data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(
            filter=returns_fbo.GetReturnsCompanyFBOFilter(),
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_list",
        data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(
            filter=returns_fbo.GetReturnsCompanyFBOFilter(
                status=[],
            ),
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(
            filter=returns_fbo.GetReturnsCompanyFBOFilter(
                posting_number="12",
                status=["one", "two"],
            ),
            offset=23,
            limit=42,
        ),
    ),

    # returns_fbs.PaginatedGetReturnsCompanyFBSFilter
    _RequestsTestCase(
        kind="second_level_empty",
        data=returns_fbs.PaginatedGetReturnsCompanyFBSFilter(
            filter=returns_fbs.GetReturnsCompanyFBSFilter(),
            offset=23,
            limit=42,
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_list",
        data=returns_fbs.PaginatedGetReturnsCompanyFBSFilter(
            filter=returns_fbs.GetReturnsCompanyFBSFilter(
                accepted_from_customer_moment=[],
                last_free_waiting_day=[],
            ),
            offset=23,
            limit=42,
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=returns_fbs.PaginatedGetReturnsCompanyFBSFilter(
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
    ),

    # stocks.PaginatedProductFilter
    _RequestsTestCase(
        kind="second_level_empty",
        data=stocks.PaginatedProductFilter(
            filter=stocks.ProductFilter(),
            cursor="23",
            limit=42,
        ),
    ),
    _RequestsTestCase(
        kind="second_level_empty_list",
        data=stocks.PaginatedProductFilter(
            filter=stocks.ProductFilter(
                offer_id=[],
                product_id=[],
                visibility="visibility",
                with_quant=stocks.ProductFilterWithQuant(),
            ),
            cursor="23",
            limit=42,
        ),
    ),
    _RequestsTestCase(
        kind="full",
        data=stocks.PaginatedProductFilter(
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
    ),
]


class TestRequests(unittest.TestCase):
    def test_requests(self) -> None:
        for test_case in _REQUESTS_TEST_CASES:
            data_name = common.get_full_qualified_name(test_case.data)
            test_case_name = f"{data_name} [{test_case.kind}]"

            with self.subTest(test_case_name):
                expected_json_filename = f"{test_case.kind}.json"
                expected_json_path = _TEST_DATA_PATH.joinpath(
                    common.get_last_module(test_case.data),
                    common.get_qualified_name(test_case.data),
                    expected_json_filename,
                )

                with open(expected_json_path) as expected_json_file:
                    expected_json = expected_json_file.read().strip()

                actual_json = test_case.data.to_json(indent=2)

                self.assertMultiLineEqual(expected_json, actual_json)
