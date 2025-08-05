import datetime
import unittest
import http

from . import common
from .test_server_handler import create_error_response
from .test_server import TestServer
from .integration_test_case import IntegrationTestCase
from ..common import request_api
from ..common import http_error
from .. import (
    actions_candidates, # + iterative
    actions_products, # + iterative
    actions,
    chat_send_message,
    chat_start,
    fbs_act_get_postings,
    posting_fbo_list, # + iterative
    posting_fbs_act_check_status,
    posting_fbs_act_create,
    posting_fbs_act_get_barcode,
    posting_fbs_get,
    posting_fbs_list, # + iterative
    posting_fbs_package_label,
    posting_fbs_product_country_list,
    posting_fbs_product_country_set,
    posting_fbs_ship_gtd,
    product_description,
    product_import_prices,
    product_import_stocks,
    product_info_attributes, # + iterative
    product_info,
    product_pictures_import,
    products_stocks,
    returns_fbo, # + iterative
    returns_fbs, # + iterative
    stocks, # + iterative
)


_TEST_ERROR_RESPONSE = create_error_response(http.HTTPStatus.UNAUTHORIZED)
_TEST_HTTP_ERROR = http_error.HTTPError(
    message=_TEST_ERROR_RESPONSE.to_json(),
    status=_TEST_ERROR_RESPONSE.code if _TEST_ERROR_RESPONSE.code is not None else 500,
    response_data=_TEST_ERROR_RESPONSE,
)
_INTEGRATION_TEST_CASES: list[IntegrationTestCase] = [
    # actions_candidates
    IntegrationTestCase(
        kind="success",
        requester=actions_candidates.get_actions_candidates,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=actions_candidates.PaginatedCandidatesForActions(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/candidates",
        response_cls=actions_candidates.GetActionsCandidatesResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="iterative",
        requester=actions_candidates.get_actions_candidates_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=actions_candidates.PaginatedCandidatesForActions(
            action_id=1.2,
            limit=2.0,
            offset=0.0,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/candidates",
        response_cls=actions_candidates.GetActionsCandidatesResponseResultWrapper,
        step_count=3,
        expected_response_items=[
            actions_candidates.GetActionsCandidatesResponseProducts(
                id=100.5,
                price=101.2,
                action_price=102.3,
                max_action_price=104.2,
                add_mode="add mode #1",
                min_stock=150.5,
                stock=151.2,
            ),
            actions_candidates.GetActionsCandidatesResponseProducts(
                id=200.5,
                price=201.2,
                action_price=202.3,
                max_action_price=204.2,
                add_mode="add mode #2",
                min_stock=250.5,
                stock=251.2,
            ),
            actions_candidates.GetActionsCandidatesResponseProducts(
                id=300.5,
                price=301.2,
                action_price=302.3,
                max_action_price=304.2,
                add_mode="add mode #3",
                min_stock=350.5,
                stock=351.2,
            ),
            actions_candidates.GetActionsCandidatesResponseProducts(
                id=400.5,
                price=401.2,
                action_price=402.3,
                max_action_price=404.2,
                add_mode="add mode #4",
                min_stock=450.5,
                stock=451.2,
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=actions_candidates.get_actions_candidates,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=actions_candidates.PaginatedCandidatesForActions(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/candidates",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # actions_products
    IntegrationTestCase(
        kind="success",
        requester=actions_products.get_action_products,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=actions_products.PaginatedActionProducts(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/products",
        response_cls=actions_products.GetSellerProductResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="iterative",
        requester=actions_products.get_action_products_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=actions_products.PaginatedActionProducts(
            action_id=1.2,
            limit=2.0,
            offset=0.0,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/products",
        response_cls=actions_products.GetSellerProductResponseResultWrapper,
        step_count=3,
        expected_response_items=[
            actions_products.GetSellerProductResponseProducts(
                id=105,
                price=101.2,
                action_price=102.3,
                max_action_price=104.2,
                add_mode="add mode #1",
                min_stock=150.5,
                stock=151.2,
            ),
            actions_products.GetSellerProductResponseProducts(
                id=205,
                price=201.2,
                action_price=202.3,
                max_action_price=204.2,
                add_mode="add mode #2",
                min_stock=250.5,
                stock=251.2,
            ),
            actions_products.GetSellerProductResponseProducts(
                id=305,
                price=301.2,
                action_price=302.3,
                max_action_price=304.2,
                add_mode="add mode #3",
                min_stock=350.5,
                stock=351.2,
            ),
            actions_products.GetSellerProductResponseProducts(
                id=405,
                price=401.2,
                action_price=402.3,
                max_action_price=404.2,
                add_mode="add mode #4",
                min_stock=450.5,
                stock=451.2,
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=actions_products.get_action_products,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=actions_products.PaginatedActionProducts(
            action_id=1.2,
            limit=2.3,
            offset=4.2,
        ),
        expected_method="POST",
        expected_endpoint="/v1/actions/products",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # actions
    IntegrationTestCase(
        kind="success",
        requester=actions.get_actions,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=None,
        expected_method="GET",
        expected_endpoint="/v1/actions",
        response_cls=actions.GetSellerActionsResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=actions.get_actions,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=None,
        expected_method="GET",
        expected_endpoint="/v1/actions",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # chat_send_message
    IntegrationTestCase(
        kind="success",
        requester=chat_send_message.send_message,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=chat_send_message.ChatMessageData(
            chat_id="23",
            text="test",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/send/message",
        response_cls=chat_send_message.GetChatStartResponseResult,
    ),
    IntegrationTestCase(
        kind="error",
        requester=chat_send_message.send_message,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=chat_send_message.ChatMessageData(
            chat_id="23",
            text="test",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/send/message",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # chat_start
    IntegrationTestCase(
        kind="success",
        requester=chat_start.get_chat_id,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=chat_start.ChatStartData(
            posting_number="23",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/start",
        response_cls=chat_start.GetChatStartResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=chat_start.get_chat_id,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=chat_start.ChatStartData(
            posting_number="23",
        ),
        expected_method="POST",
        expected_endpoint="/v1/chat/start",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # fbs_act_get_postings
    IntegrationTestCase(
        kind="success",
        requester=fbs_act_get_postings.get_posting_fbs_act_data,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=fbs_act_get_postings.PostingFBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-postings",
        response_cls=fbs_act_get_postings.PostingFBSActDataResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=fbs_act_get_postings.get_posting_fbs_act_data,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=fbs_act_get_postings.PostingFBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-postings",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbo_list
    IntegrationTestCase(
        kind="success",
        requester=posting_fbo_list.get_posting_fbo_list,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=posting_fbo_list.get_posting_fbo_list_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
            limit=2,
            offset=0,
            with_=posting_fbo_list.PostingAdditionalFields(
                analytics_data=True,
                financial_data=True,
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbo/list",
        response_cls=posting_fbo_list.GetPostingFBOListResponseResultWrapper,
        step_count=3,
        expected_response_items=[
            posting_fbo_list.GetPostingFBOListResponseResult(
                additional_data=[
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #1001",
                        value="value #1001",
                    ),
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #1002",
                        value="value #1002",
                    ),
                ],
                analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                    city="city #1001",
                    delivery_type="delivery type #1001",
                    is_legal=False,
                    is_premium=False,
                    payment_type_group_name="payment type group name #1001",
                    region="region #1001",
                    warehouse_id=1001023,
                    warehouse_name="warehouse name #1001",
                ),
                cancel_reason_id=100105,
                financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                    posting_services=\
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=1001.01,
                            marketplace_service_item_direct_flow_trans=1001.02,
                            marketplace_service_item_dropoff_ff=1001.03,
                            marketplace_service_item_dropoff_pvz=1001.04,
                            marketplace_service_item_dropoff_sc=1001.05,
                            marketplace_service_item_fulfillment=1001.06,
                            marketplace_service_item_pickup=1001.07,
                            marketplace_service_item_return_after_deliv_to_customer=1001.08,
                            marketplace_service_item_return_flow_trans=1001.09,
                            marketplace_service_item_return_not_deliv_to_customer=1001.10,
                            marketplace_service_item_return_part_goods_customer=1001.11,
                        ),
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #1001", "action #1002"],
                            client_price="100100005",
                            commission_amount=10010.01,
                            commission_percent=100100012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=100100.01,
                                    marketplace_service_item_direct_flow_trans=100100.02,
                                    marketplace_service_item_dropoff_ff=100100.03,
                                    marketplace_service_item_dropoff_pvz=100100.04,
                                    marketplace_service_item_dropoff_sc=100100.05,
                                    marketplace_service_item_fulfillment=100100.06,
                                    marketplace_service_item_pickup=100100.07,
                                    marketplace_service_item_return_after_deliv_to_customer=100100.08,
                                    marketplace_service_item_return_flow_trans=100100.09,
                                    marketplace_service_item_return_not_deliv_to_customer=100100.10,
                                    marketplace_service_item_return_part_goods_customer=100100.11,
                                ),
                            old_price=10010.02,
                            payout=10010.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=100100.12,
                                tag="tag #1001",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T19:04:05.999999+07:00",
                                ),
                            ),
                            price=10010.04,
                            product_id=100100023,
                            quantity=100100042,
                            total_discount_percent=10010.05,
                            total_discount_value=10010.06,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #1003", "action #1004"],
                            client_price="100200005",
                            commission_amount=10020.01,
                            commission_percent=100200012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=100200.01,
                                    marketplace_service_item_direct_flow_trans=100200.02,
                                    marketplace_service_item_dropoff_ff=100200.03,
                                    marketplace_service_item_dropoff_pvz=100200.04,
                                    marketplace_service_item_dropoff_sc=100200.05,
                                    marketplace_service_item_fulfillment=100200.06,
                                    marketplace_service_item_pickup=100200.07,
                                    marketplace_service_item_return_after_deliv_to_customer=100200.08,
                                    marketplace_service_item_return_flow_trans=100200.09,
                                    marketplace_service_item_return_not_deliv_to_customer=100200.10,
                                    marketplace_service_item_return_part_goods_customer=100200.11,
                                ),
                            old_price=10020.02,
                            payout=10020.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=100200.12,
                                tag="tag #1002",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T21:04:05.999999+07:00",
                                ),
                            ),
                            price=10020.04,
                            product_id=100200023,
                            quantity=100200042,
                            total_discount_percent=10020.05,
                            total_discount_value=10020.06,
                        ),
                    ],
                ),
                order_id=100112,
                order_number="100123",
                posting_number="100142",
                products=[
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #1001", "digital code #1002"],
                        name="name #1001",
                        offer_id="10010005",
                        price="10010012",
                        quantity=10010023,
                        sku=10010042,
                    ),
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #1003", "digital code #1004"],
                        name="name #1002",
                        offer_id="10020005",
                        price="10020012",
                        quantity=10020023,
                        sku=10020042,
                    ),
                ],
                status="status #1001",
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
            ),
            posting_fbo_list.GetPostingFBOListResponseResult(
                additional_data=[
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #1003",
                        value="value #1003",
                    ),
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #1004",
                        value="value #1004",
                    ),
                ],
                analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                    city="city #1002",
                    delivery_type="delivery type #1002",
                    is_legal=True,
                    is_premium=True,
                    payment_type_group_name="payment type group name #1002",
                    region="region #1002",
                    warehouse_id=1002023,
                    warehouse_name="warehouse name #1002",
                ),
                cancel_reason_id=100205,
                financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                    posting_services=\
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=1002.01,
                            marketplace_service_item_direct_flow_trans=1002.02,
                            marketplace_service_item_dropoff_ff=1002.03,
                            marketplace_service_item_dropoff_pvz=1002.04,
                            marketplace_service_item_dropoff_sc=1002.05,
                            marketplace_service_item_fulfillment=1002.06,
                            marketplace_service_item_pickup=1002.07,
                            marketplace_service_item_return_after_deliv_to_customer=1002.08,
                            marketplace_service_item_return_flow_trans=1002.09,
                            marketplace_service_item_return_not_deliv_to_customer=1002.10,
                            marketplace_service_item_return_part_goods_customer=1002.11,
                        ),
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #1005", "action #1006"],
                            client_price="100300005",
                            commission_amount=10030.01,
                            commission_percent=100300012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=100300.01,
                                    marketplace_service_item_direct_flow_trans=100300.02,
                                    marketplace_service_item_dropoff_ff=100300.03,
                                    marketplace_service_item_dropoff_pvz=100300.04,
                                    marketplace_service_item_dropoff_sc=100300.05,
                                    marketplace_service_item_fulfillment=100300.06,
                                    marketplace_service_item_pickup=100300.07,
                                    marketplace_service_item_return_after_deliv_to_customer=100300.08,
                                    marketplace_service_item_return_flow_trans=100300.09,
                                    marketplace_service_item_return_not_deliv_to_customer=100300.10,
                                    marketplace_service_item_return_part_goods_customer=100300.11,
                                ),
                            old_price=10030.02,
                            payout=10030.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=100300.12,
                                tag="tag #1001",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T19:04:05.999999+07:00",
                                ),
                            ),
                            price=10030.04,
                            product_id=100300023,
                            quantity=100300042,
                            total_discount_percent=10030.05,
                            total_discount_value=10030.06,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #1007", "action #1008"],
                            client_price="100400005",
                            commission_amount=10040.01,
                            commission_percent=100400012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=100400.01,
                                    marketplace_service_item_direct_flow_trans=100400.02,
                                    marketplace_service_item_dropoff_ff=100400.03,
                                    marketplace_service_item_dropoff_pvz=100400.04,
                                    marketplace_service_item_dropoff_sc=100400.05,
                                    marketplace_service_item_fulfillment=100400.06,
                                    marketplace_service_item_pickup=100400.07,
                                    marketplace_service_item_return_after_deliv_to_customer=100400.08,
                                    marketplace_service_item_return_flow_trans=100400.09,
                                    marketplace_service_item_return_not_deliv_to_customer=100400.10,
                                    marketplace_service_item_return_part_goods_customer=100400.11,
                                ),
                            old_price=10040.02,
                            payout=10040.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=100400.12,
                                tag="tag #1002",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T21:04:05.999999+07:00",
                                ),
                            ),
                            price=10040.04,
                            product_id=100400023,
                            quantity=100400042,
                            total_discount_percent=10040.05,
                            total_discount_value=10040.06,
                        ),
                    ],
                ),
                order_id=100212,
                order_number="100223",
                posting_number="100242",
                products=[
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #1005", "digital code #1006"],
                        name="name #1003",
                        offer_id="10030005",
                        price="10030012",
                        quantity=10030023,
                        sku=10030042,
                    ),
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #1007", "digital code #1008"],
                        name="name #1004",
                        offer_id="10040005",
                        price="10040012",
                        quantity=10040023,
                        sku=10040042,
                    ),
                ],
                status="status #1002",
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-03T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-03T17:04:05.999999+07:00",
                ),
            ),
            posting_fbo_list.GetPostingFBOListResponseResult(
                additional_data=[
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #2001",
                        value="value #2001",
                    ),
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #2002",
                        value="value #2002",
                    ),
                ],
                analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                    city="city #2001",
                    delivery_type="delivery type #2001",
                    is_legal=False,
                    is_premium=False,
                    payment_type_group_name="payment type group name #2001",
                    region="region #2001",
                    warehouse_id=2001023,
                    warehouse_name="warehouse name #2001",
                ),
                cancel_reason_id=200105,
                financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                    posting_services=\
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=2001.01,
                            marketplace_service_item_direct_flow_trans=2001.02,
                            marketplace_service_item_dropoff_ff=2001.03,
                            marketplace_service_item_dropoff_pvz=2001.04,
                            marketplace_service_item_dropoff_sc=2001.05,
                            marketplace_service_item_fulfillment=2001.06,
                            marketplace_service_item_pickup=2001.07,
                            marketplace_service_item_return_after_deliv_to_customer=2001.08,
                            marketplace_service_item_return_flow_trans=2001.09,
                            marketplace_service_item_return_not_deliv_to_customer=2001.10,
                            marketplace_service_item_return_part_goods_customer=2001.11,
                        ),
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #2001", "action #2002"],
                            client_price="200100005",
                            commission_amount=20010.01,
                            commission_percent=200100012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=200100.01,
                                    marketplace_service_item_direct_flow_trans=200100.02,
                                    marketplace_service_item_dropoff_ff=200100.03,
                                    marketplace_service_item_dropoff_pvz=200100.04,
                                    marketplace_service_item_dropoff_sc=200100.05,
                                    marketplace_service_item_fulfillment=200100.06,
                                    marketplace_service_item_pickup=200100.07,
                                    marketplace_service_item_return_after_deliv_to_customer=200100.08,
                                    marketplace_service_item_return_flow_trans=200100.09,
                                    marketplace_service_item_return_not_deliv_to_customer=200100.10,
                                    marketplace_service_item_return_part_goods_customer=200100.11,
                                ),
                            old_price=20010.02,
                            payout=20010.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=200100.12,
                                tag="tag #2001",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T19:04:05.999999+07:00",
                                ),
                            ),
                            price=20010.04,
                            product_id=200100023,
                            quantity=200100042,
                            total_discount_percent=20010.05,
                            total_discount_value=20010.06,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #2003", "action #2004"],
                            client_price="200200005",
                            commission_amount=20020.01,
                            commission_percent=200200012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=200200.01,
                                    marketplace_service_item_direct_flow_trans=200200.02,
                                    marketplace_service_item_dropoff_ff=200200.03,
                                    marketplace_service_item_dropoff_pvz=200200.04,
                                    marketplace_service_item_dropoff_sc=200200.05,
                                    marketplace_service_item_fulfillment=200200.06,
                                    marketplace_service_item_pickup=200200.07,
                                    marketplace_service_item_return_after_deliv_to_customer=200200.08,
                                    marketplace_service_item_return_flow_trans=200200.09,
                                    marketplace_service_item_return_not_deliv_to_customer=200200.10,
                                    marketplace_service_item_return_part_goods_customer=200200.11,
                                ),
                            old_price=20020.02,
                            payout=20020.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=200200.12,
                                tag="tag #2002",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T21:04:05.999999+07:00",
                                ),
                            ),
                            price=20020.04,
                            product_id=200200023,
                            quantity=200200042,
                            total_discount_percent=20020.05,
                            total_discount_value=20020.06,
                        ),
                    ],
                ),
                order_id=200112,
                order_number="200123",
                posting_number="200142",
                products=[
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #2001", "digital code #2002"],
                        name="name #2001",
                        offer_id="20010005",
                        price="20010012",
                        quantity=20010023,
                        sku=20010042,
                    ),
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #2003", "digital code #2004"],
                        name="name #2002",
                        offer_id="20020005",
                        price="20020012",
                        quantity=20020023,
                        sku=20020042,
                    ),
                ],
                status="status #2001",
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
            ),
            posting_fbo_list.GetPostingFBOListResponseResult(
                additional_data=[
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #2003",
                        value="value #2003",
                    ),
                    posting_fbo_list.GetPostingFBOAdditionalDataItem(
                        key="key #2004",
                        value="value #2004",
                    ),
                ],
                analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                    city="city #2002",
                    delivery_type="delivery type #2002",
                    is_legal=True,
                    is_premium=True,
                    payment_type_group_name="payment type group name #2002",
                    region="region #2002",
                    warehouse_id=2002023,
                    warehouse_name="warehouse name #2002",
                ),
                cancel_reason_id=200205,
                financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                    posting_services=\
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=2002.01,
                            marketplace_service_item_direct_flow_trans=2002.02,
                            marketplace_service_item_dropoff_ff=2002.03,
                            marketplace_service_item_dropoff_pvz=2002.04,
                            marketplace_service_item_dropoff_sc=2002.05,
                            marketplace_service_item_fulfillment=2002.06,
                            marketplace_service_item_pickup=2002.07,
                            marketplace_service_item_return_after_deliv_to_customer=2002.08,
                            marketplace_service_item_return_flow_trans=2002.09,
                            marketplace_service_item_return_not_deliv_to_customer=2002.10,
                            marketplace_service_item_return_part_goods_customer=2002.11,
                        ),
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #2005", "action #2006"],
                            client_price="200300005",
                            commission_amount=20030.01,
                            commission_percent=200300012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=200300.01,
                                    marketplace_service_item_direct_flow_trans=200300.02,
                                    marketplace_service_item_dropoff_ff=200300.03,
                                    marketplace_service_item_dropoff_pvz=200300.04,
                                    marketplace_service_item_dropoff_sc=200300.05,
                                    marketplace_service_item_fulfillment=200300.06,
                                    marketplace_service_item_pickup=200300.07,
                                    marketplace_service_item_return_after_deliv_to_customer=200300.08,
                                    marketplace_service_item_return_flow_trans=200300.09,
                                    marketplace_service_item_return_not_deliv_to_customer=200300.10,
                                    marketplace_service_item_return_part_goods_customer=200300.11,
                                ),
                            old_price=20030.02,
                            payout=20030.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=200300.12,
                                tag="tag #2001",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T19:04:05.999999+07:00",
                                ),
                            ),
                            price=20030.04,
                            product_id=200300023,
                            quantity=200300042,
                            total_discount_percent=20030.05,
                            total_discount_value=20030.06,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                            actions=["action #2007", "action #2008"],
                            client_price="200400005",
                            commission_amount=20040.01,
                            commission_percent=200400012,
                            item_services=\
                                posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=200400.01,
                                    marketplace_service_item_direct_flow_trans=200400.02,
                                    marketplace_service_item_dropoff_ff=200400.03,
                                    marketplace_service_item_dropoff_pvz=200400.04,
                                    marketplace_service_item_dropoff_sc=200400.05,
                                    marketplace_service_item_fulfillment=200400.06,
                                    marketplace_service_item_pickup=200400.07,
                                    marketplace_service_item_return_after_deliv_to_customer=200400.08,
                                    marketplace_service_item_return_flow_trans=200400.09,
                                    marketplace_service_item_return_not_deliv_to_customer=200400.10,
                                    marketplace_service_item_return_part_goods_customer=200400.11,
                                ),
                            old_price=20040.02,
                            payout=20040.03,
                            picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                amount=200400.12,
                                tag="tag #2002",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T21:04:05.999999+07:00",
                                ),
                            ),
                            price=20040.04,
                            product_id=200400023,
                            quantity=200400042,
                            total_discount_percent=20040.05,
                            total_discount_value=20040.06,
                        ),
                    ],
                ),
                order_id=200212,
                order_number="200223",
                posting_number="200242",
                products=[
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #2005", "digital code #2006"],
                        name="name #2003",
                        offer_id="20030005",
                        price="20030012",
                        quantity=20030023,
                        sku=20030042,
                    ),
                    posting_fbo_list.GetPostingFBOListResponseProduct(
                        digital_codes=["digital code #2007", "digital code #2008"],
                        name="name #2004",
                        offer_id="20040005",
                        price="20040012",
                        quantity=20040023,
                        sku=20040042,
                    ),
                ],
                status="status #2002",
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-03T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-03T17:04:05.999999+07:00",
                ),
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbo_list.get_posting_fbo_list,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_act_check_status
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_check_status.create_posting_fbs_act,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_act_check_status.PostingFSBActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/check-status",
        response_cls=posting_fbs_act_check_status.PostingFBSActCreateResponseActResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_act_check_status.create_posting_fbs_act,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_act_check_status.PostingFSBActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/check-status",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_act_create
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_create.create_posting_fbs_act,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_act_create.create_posting_fbs_act,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_act_create.PostingFSBDeliveryData(
            containers_count=23,
            delivery_method_id=42,
            departure_date=datetime.datetime.fromisoformat(
                "2006-01-02T15:04:05.999999+07:00",
            ),
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/create",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_act_get_barcode
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_act_get_barcode.get_posting_fbs_act_barcode,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_act_get_barcode.FBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-barcode",
        response_cls=None,
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_act_get_barcode.get_posting_fbs_act_barcode,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_act_get_barcode.FBSActData(
            id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/act/get-barcode",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_get
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_get.get_posting_fbs_data,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_get.get_posting_fbs_data,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_list
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=posting_fbs_list.get_posting_fbs_list_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
            limit=2,
            offset=0,
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
        step_count=3,
        expected_response_items=[
            posting_fbs_list.GetPostingFBSListResponsePosting(
                addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                    name="name #10011",
                    phone="phone #10011",
                ),
                analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                    city="city #10011",
                    is_premium=False,
                    payment_type_group_name="payment type group name #10011",
                    region="region #10011",
                    tpl_provider="tpl provider #10011",
                    tpl_provider_id=10011023,
                    warehouse="warehouse #10011",
                    warehouse_id=10011042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-03T01:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                    lower_barcode="lower barcode #10011",
                    upper_barcode="upper barcode #10011",
                ),
                cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                    affect_cancellation_rating=False,
                    cancel_reason="cancel reason #10011",
                    cancel_reason_id=10012023,
                    cancellation_initiator="cancellation initiator #10011",
                    cancellation_type="cancellation type #10011",
                    cancelled_after_ship=False,
                ),
                customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                    address=posting_fbs_list.GetPostingFBSListResponseAddress(
                        address_tail="address tail #10011",
                        city="city #10012",
                        comment="comment #10011",
                        country="country #10011",
                        district="district #10011",
                        latitude=10011.01,
                        longitude=10011.02,
                        provider_pvz_code="provider pvz code #10011",
                        pvz_code=10013042,
                        region="region #10011",
                        zip_code="zip code #10011",
                    ),
                    customer_email="customer email #10011",
                    customer_id=10013023,
                    name="name #10012",
                    phone="phone #10012",
                ),
                delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                    id=10014012,
                    name="name #10013",
                    tpl_provider="tpl provider #10012",
                    tpl_provider_id=10014023,
                    warehouse="warehouse #10012",
                    warehouse_id=10014042,
                ),
                financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                    posting_services=\
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=10011.03,
                            marketplace_service_item_direct_flow_trans=10011.04,
                            marketplace_service_item_dropoff_ff=10011.05,
                            marketplace_service_item_dropoff_pvz=10011.06,
                            marketplace_service_item_dropoff_sc=10011.07,
                            marketplace_service_item_fulfillment=10011.08,
                            marketplace_service_item_pickup=10011.09,
                            marketplace_service_item_return_after_deliv_to_customer=10011.10,
                            marketplace_service_item_return_flow_trans=10011.11,
                            marketplace_service_item_return_not_deliv_to_customer=10011.12,
                            marketplace_service_item_return_part_goods_customer=10011.13,
                        ),
                    products=[
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #1001", "action #1002"],
                            client_price="10017005",
                            commission_amount=10011.14,
                            commission_percent=10017012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=10011.20,
                                    marketplace_service_item_direct_flow_trans=10011.21,
                                    marketplace_service_item_dropoff_ff=10011.22,
                                    marketplace_service_item_dropoff_pvz=10011.23,
                                    marketplace_service_item_dropoff_sc=10011.24,
                                    marketplace_service_item_fulfillment=10011.25,
                                    marketplace_service_item_pickup=10011.26,
                                    marketplace_service_item_return_after_deliv_to_customer=10011.27,
                                    marketplace_service_item_return_flow_trans=10011.28,
                                    marketplace_service_item_return_not_deliv_to_customer=10011.29,
                                    marketplace_service_item_return_part_goods_customer=10011.30,
                                ),
                            old_price=10011.15,
                            payout=10011.16,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=10011.31,
                                tag="tag #10011",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T21:04:05.999999+07:00",
                                ),
                            ),
                            price=10011.17,
                            product_id=10017023,
                            quantity=10017042,
                            total_discount_percent=10011.18,
                            total_discount_value=10011.19,
                        ),
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #1003", "action #1004"],
                            client_price="10018005",
                            commission_amount=10011.32,
                            commission_percent=10018012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=10011.38,
                                    marketplace_service_item_direct_flow_trans=10011.39,
                                    marketplace_service_item_dropoff_ff=10011.40,
                                    marketplace_service_item_dropoff_pvz=10011.41,
                                    marketplace_service_item_dropoff_sc=10011.42,
                                    marketplace_service_item_fulfillment=10011.43,
                                    marketplace_service_item_pickup=10011.44,
                                    marketplace_service_item_return_after_deliv_to_customer=10011.45,
                                    marketplace_service_item_return_flow_trans=10011.46,
                                    marketplace_service_item_return_not_deliv_to_customer=10011.47,
                                    marketplace_service_item_return_part_goods_customer=10011.48,
                                ),
                            old_price=10011.33,
                            payout=10011.34,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=10011.49,
                                tag="tag #10012",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T23:04:05.999999+07:00",
                                ),
                            ),
                            price=10011.35,
                            product_id=10018023,
                            quantity=10018042,
                            total_discount_percent=10011.36,
                            total_discount_value=10011.37,
                        ),
                    ],
                ),
                is_express=False,
                order_id=100105,
                order_number="100112",
                posting_number="100123",
                products=[
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #1001", "mandatory mark #1002"],
                        name="name #10014",
                        offer_id="10015005",
                        price="10015012",
                        quantity=10015023,
                        sku=10015042,
                        currency_code="currency code #10011",
                    ),
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #1003", "mandatory mark #1004"],
                        name="name #10015",
                        offer_id="10016005",
                        price="10016012",
                        quantity=10016023,
                        sku=10016042,
                        currency_code="currency code #10012",
                    ),
                ],
                requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                    products_requiring_gtd=[19001, 19002],
                    products_requiring_country=[19003, 19004],
                    products_requiring_mandatory_mark=[19005, 19006],
                    products_requiring_rnpt=[19007, 19008],
                ),
                status="status #1001",
                tpl_integration_type="tpl integration type #1001",
                tracking_number="100142",
                delivering_date=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
                shipment_date=datetime.datetime.fromisoformat(
                    "2006-01-02T19:04:05.999999+07:00",
                ),
            ),
            posting_fbs_list.GetPostingFBSListResponsePosting(
                addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                    name="name #10021",
                    phone="phone #10021",
                ),
                analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                    city="city #10021",
                    is_premium=True,
                    payment_type_group_name="payment type group name #10021",
                    region="region #10021",
                    tpl_provider="tpl provider #10021",
                    tpl_provider_id=10021023,
                    warehouse="warehouse #10021",
                    warehouse_id=10021042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-04T01:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                    lower_barcode="lower barcode #10021",
                    upper_barcode="upper barcode #10021",
                ),
                cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                    affect_cancellation_rating=True,
                    cancel_reason="cancel reason #10021",
                    cancel_reason_id=10022023,
                    cancellation_initiator="cancellation initiator #10021",
                    cancellation_type="cancellation type #10021",
                    cancelled_after_ship=True,
                ),
                customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                    address=posting_fbs_list.GetPostingFBSListResponseAddress(
                        address_tail="address tail #10021",
                        city="city #10022",
                        comment="comment #10021",
                        country="country #10021",
                        district="district #10021",
                        latitude=10021.01,
                        longitude=10021.02,
                        provider_pvz_code="provider pvz code #10021",
                        pvz_code=10023042,
                        region="region #10021",
                        zip_code="zip code #10021",
                    ),
                    customer_email="customer email #10021",
                    customer_id=10023023,
                    name="name #10022",
                    phone="phone #10022",
                ),
                delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                    id=10024012,
                    name="name #10023",
                    tpl_provider="tpl provider #10022",
                    tpl_provider_id=10024023,
                    warehouse="warehouse #10022",
                    warehouse_id=10024042,
                ),
                financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                    posting_services=\
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=10021.03,
                            marketplace_service_item_direct_flow_trans=10021.04,
                            marketplace_service_item_dropoff_ff=10021.05,
                            marketplace_service_item_dropoff_pvz=10021.06,
                            marketplace_service_item_dropoff_sc=10021.07,
                            marketplace_service_item_fulfillment=10021.08,
                            marketplace_service_item_pickup=10021.09,
                            marketplace_service_item_return_after_deliv_to_customer=10021.10,
                            marketplace_service_item_return_flow_trans=10021.11,
                            marketplace_service_item_return_not_deliv_to_customer=10021.12,
                            marketplace_service_item_return_part_goods_customer=10021.13,
                        ),
                    products=[
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #1005", "action #1006"],
                            client_price="10027005",
                            commission_amount=10021.14,
                            commission_percent=10027012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=10021.20,
                                    marketplace_service_item_direct_flow_trans=10021.21,
                                    marketplace_service_item_dropoff_ff=10021.22,
                                    marketplace_service_item_dropoff_pvz=10021.23,
                                    marketplace_service_item_dropoff_sc=10021.24,
                                    marketplace_service_item_fulfillment=10021.25,
                                    marketplace_service_item_pickup=10021.26,
                                    marketplace_service_item_return_after_deliv_to_customer=10021.27,
                                    marketplace_service_item_return_flow_trans=10021.28,
                                    marketplace_service_item_return_not_deliv_to_customer=10021.29,
                                    marketplace_service_item_return_part_goods_customer=10021.30,
                                ),
                            old_price=10021.15,
                            payout=10021.16,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=10021.31,
                                tag="tag #10021",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T21:04:05.999999+07:00",
                                ),
                            ),
                            price=10021.17,
                            product_id=10027023,
                            quantity=10027042,
                            total_discount_percent=10021.18,
                            total_discount_value=10021.19,
                        ),
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #1007", "action #1008"],
                            client_price="10028005",
                            commission_amount=10021.32,
                            commission_percent=10028012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=10021.38,
                                    marketplace_service_item_direct_flow_trans=10021.39,
                                    marketplace_service_item_dropoff_ff=10021.40,
                                    marketplace_service_item_dropoff_pvz=10021.41,
                                    marketplace_service_item_dropoff_sc=10021.42,
                                    marketplace_service_item_fulfillment=10021.43,
                                    marketplace_service_item_pickup=10021.44,
                                    marketplace_service_item_return_after_deliv_to_customer=10021.45,
                                    marketplace_service_item_return_flow_trans=10021.46,
                                    marketplace_service_item_return_not_deliv_to_customer=10021.47,
                                    marketplace_service_item_return_part_goods_customer=10021.48,
                                ),
                            old_price=10021.33,
                            payout=10021.34,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=10021.49,
                                tag="tag #10022",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T23:04:05.999999+07:00",
                                ),
                            ),
                            price=10021.35,
                            product_id=10028023,
                            quantity=10028042,
                            total_discount_percent=10021.36,
                            total_discount_value=10021.37,
                        ),
                    ],
                ),
                is_express=True,
                order_id=100205,
                order_number="100212",
                posting_number="100223",
                products=[
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #1005", "mandatory mark #1006"],
                        name="name #10024",
                        offer_id="10025005",
                        price="10025012",
                        quantity=10025023,
                        sku=10025042,
                        currency_code="currency code #10021",
                    ),
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #1007", "mandatory mark #1008"],
                        name="name #10025",
                        offer_id="10026005",
                        price="10026012",
                        quantity=10026023,
                        sku=10026042,
                        currency_code="currency code #10022",
                    ),
                ],
                requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                    products_requiring_gtd=[29001, 29002],
                    products_requiring_country=[29003, 29004],
                    products_requiring_mandatory_mark=[29005, 29006],
                    products_requiring_rnpt=[29007, 29008],
                ),
                status="status #1002",
                tpl_integration_type="tpl integration type #1002",
                tracking_number="100242",
                delivering_date=datetime.datetime.fromisoformat(
                    "2006-01-03T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-03T17:04:05.999999+07:00",
                ),
                shipment_date=datetime.datetime.fromisoformat(
                    "2006-01-03T19:04:05.999999+07:00",
                ),
            ),
            posting_fbs_list.GetPostingFBSListResponsePosting(
                addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                    name="name #20011",
                    phone="phone #20011",
                ),
                analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                    city="city #20011",
                    is_premium=False,
                    payment_type_group_name="payment type group name #20011",
                    region="region #20011",
                    tpl_provider="tpl provider #20011",
                    tpl_provider_id=20011023,
                    warehouse="warehouse #20011",
                    warehouse_id=20011042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-03T01:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                    lower_barcode="lower barcode #20011",
                    upper_barcode="upper barcode #20011",
                ),
                cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                    affect_cancellation_rating=False,
                    cancel_reason="cancel reason #20011",
                    cancel_reason_id=20012023,
                    cancellation_initiator="cancellation initiator #20011",
                    cancellation_type="cancellation type #20011",
                    cancelled_after_ship=False,
                ),
                customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                    address=posting_fbs_list.GetPostingFBSListResponseAddress(
                        address_tail="address tail #20011",
                        city="city #20012",
                        comment="comment #20011",
                        country="country #20011",
                        district="district #20011",
                        latitude=20011.01,
                        longitude=20011.02,
                        provider_pvz_code="provider pvz code #20011",
                        pvz_code=20013042,
                        region="region #20011",
                        zip_code="zip code #20011",
                    ),
                    customer_email="customer email #20011",
                    customer_id=20013023,
                    name="name #20012",
                    phone="phone #20012",
                ),
                delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                    id=20014012,
                    name="name #20013",
                    tpl_provider="tpl provider #20012",
                    tpl_provider_id=20014023,
                    warehouse="warehouse #20012",
                    warehouse_id=20014042,
                ),
                financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                    posting_services=\
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=20011.03,
                            marketplace_service_item_direct_flow_trans=20011.04,
                            marketplace_service_item_dropoff_ff=20011.05,
                            marketplace_service_item_dropoff_pvz=20011.06,
                            marketplace_service_item_dropoff_sc=20011.07,
                            marketplace_service_item_fulfillment=20011.08,
                            marketplace_service_item_pickup=20011.09,
                            marketplace_service_item_return_after_deliv_to_customer=20011.10,
                            marketplace_service_item_return_flow_trans=20011.11,
                            marketplace_service_item_return_not_deliv_to_customer=20011.12,
                            marketplace_service_item_return_part_goods_customer=20011.13,
                        ),
                    products=[
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #2001", "action #2002"],
                            client_price="20017005",
                            commission_amount=20011.14,
                            commission_percent=20017012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=20011.20,
                                    marketplace_service_item_direct_flow_trans=20011.21,
                                    marketplace_service_item_dropoff_ff=20011.22,
                                    marketplace_service_item_dropoff_pvz=20011.23,
                                    marketplace_service_item_dropoff_sc=20011.24,
                                    marketplace_service_item_fulfillment=20011.25,
                                    marketplace_service_item_pickup=20011.26,
                                    marketplace_service_item_return_after_deliv_to_customer=20011.27,
                                    marketplace_service_item_return_flow_trans=20011.28,
                                    marketplace_service_item_return_not_deliv_to_customer=20011.29,
                                    marketplace_service_item_return_part_goods_customer=20011.30,
                                ),
                            old_price=20011.15,
                            payout=20011.16,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=20011.31,
                                tag="tag #20011",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T21:04:05.999999+07:00",
                                ),
                            ),
                            price=20011.17,
                            product_id=20017023,
                            quantity=20017042,
                            total_discount_percent=20011.18,
                            total_discount_value=20011.19,
                        ),
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #2003", "action #2004"],
                            client_price="20018005",
                            commission_amount=20011.32,
                            commission_percent=20018012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=20011.38,
                                    marketplace_service_item_direct_flow_trans=20011.39,
                                    marketplace_service_item_dropoff_ff=20011.40,
                                    marketplace_service_item_dropoff_pvz=20011.41,
                                    marketplace_service_item_dropoff_sc=20011.42,
                                    marketplace_service_item_fulfillment=20011.43,
                                    marketplace_service_item_pickup=20011.44,
                                    marketplace_service_item_return_after_deliv_to_customer=20011.45,
                                    marketplace_service_item_return_flow_trans=20011.46,
                                    marketplace_service_item_return_not_deliv_to_customer=20011.47,
                                    marketplace_service_item_return_part_goods_customer=20011.48,
                                ),
                            old_price=20011.33,
                            payout=20011.34,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=20011.49,
                                tag="tag #20012",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T23:04:05.999999+07:00",
                                ),
                            ),
                            price=20011.35,
                            product_id=20018023,
                            quantity=20018042,
                            total_discount_percent=20011.36,
                            total_discount_value=20011.37,
                        ),
                    ],
                ),
                is_express=False,
                order_id=200105,
                order_number="200112",
                posting_number="200123",
                products=[
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #2001", "mandatory mark #2002"],
                        name="name #20014",
                        offer_id="20015005",
                        price="20015012",
                        quantity=20015023,
                        sku=20015042,
                        currency_code="currency code #20011",
                    ),
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #2003", "mandatory mark #2004"],
                        name="name #20015",
                        offer_id="20016005",
                        price="20016012",
                        quantity=20016023,
                        sku=20016042,
                        currency_code="currency code #20012",
                    ),
                ],
                requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                    products_requiring_gtd=[19001, 19002],
                    products_requiring_country=[19003, 19004],
                    products_requiring_mandatory_mark=[19005, 19006],
                    products_requiring_rnpt=[19007, 19008],
                ),
                status="status #2001",
                tpl_integration_type="tpl integration type #2001",
                tracking_number="200142",
                delivering_date=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
                shipment_date=datetime.datetime.fromisoformat(
                    "2006-01-02T19:04:05.999999+07:00",
                ),
            ),
            posting_fbs_list.GetPostingFBSListResponsePosting(
                addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                    name="name #20021",
                    phone="phone #20021",
                ),
                analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                    city="city #20021",
                    is_premium=True,
                    payment_type_group_name="payment type group name #20021",
                    region="region #20021",
                    tpl_provider="tpl provider #20021",
                    tpl_provider_id=20021023,
                    warehouse="warehouse #20021",
                    warehouse_id=20021042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-04T01:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                    lower_barcode="lower barcode #20021",
                    upper_barcode="upper barcode #20021",
                ),
                cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                    affect_cancellation_rating=True,
                    cancel_reason="cancel reason #20021",
                    cancel_reason_id=20022023,
                    cancellation_initiator="cancellation initiator #20021",
                    cancellation_type="cancellation type #20021",
                    cancelled_after_ship=True,
                ),
                customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                    address=posting_fbs_list.GetPostingFBSListResponseAddress(
                        address_tail="address tail #20021",
                        city="city #20022",
                        comment="comment #20021",
                        country="country #20021",
                        district="district #20021",
                        latitude=20021.01,
                        longitude=20021.02,
                        provider_pvz_code="provider pvz code #20021",
                        pvz_code=20023042,
                        region="region #20021",
                        zip_code="zip code #20021",
                    ),
                    customer_email="customer email #20021",
                    customer_id=20023023,
                    name="name #20022",
                    phone="phone #20022",
                ),
                delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                    id=20024012,
                    name="name #20023",
                    tpl_provider="tpl provider #20022",
                    tpl_provider_id=20024023,
                    warehouse="warehouse #20022",
                    warehouse_id=20024042,
                ),
                financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                    posting_services=\
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                            marketplace_service_item_deliv_to_customer=20021.03,
                            marketplace_service_item_direct_flow_trans=20021.04,
                            marketplace_service_item_dropoff_ff=20021.05,
                            marketplace_service_item_dropoff_pvz=20021.06,
                            marketplace_service_item_dropoff_sc=20021.07,
                            marketplace_service_item_fulfillment=20021.08,
                            marketplace_service_item_pickup=20021.09,
                            marketplace_service_item_return_after_deliv_to_customer=20021.10,
                            marketplace_service_item_return_flow_trans=20021.11,
                            marketplace_service_item_return_not_deliv_to_customer=20021.12,
                            marketplace_service_item_return_part_goods_customer=20021.13,
                        ),
                    products=[
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #2005", "action #2006"],
                            client_price="20027005",
                            commission_amount=20021.14,
                            commission_percent=20027012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=20021.20,
                                    marketplace_service_item_direct_flow_trans=20021.21,
                                    marketplace_service_item_dropoff_ff=20021.22,
                                    marketplace_service_item_dropoff_pvz=20021.23,
                                    marketplace_service_item_dropoff_sc=20021.24,
                                    marketplace_service_item_fulfillment=20021.25,
                                    marketplace_service_item_pickup=20021.26,
                                    marketplace_service_item_return_after_deliv_to_customer=20021.27,
                                    marketplace_service_item_return_flow_trans=20021.28,
                                    marketplace_service_item_return_not_deliv_to_customer=20021.29,
                                    marketplace_service_item_return_part_goods_customer=20021.30,
                                ),
                            old_price=20021.15,
                            payout=20021.16,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=20021.31,
                                tag="tag #20021",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T21:04:05.999999+07:00",
                                ),
                            ),
                            price=20021.17,
                            product_id=20027023,
                            quantity=20027042,
                            total_discount_percent=20021.18,
                            total_discount_value=20021.19,
                        ),
                        posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                            actions=["action #2007", "action #2008"],
                            client_price="20028005",
                            commission_amount=20021.32,
                            commission_percent=20028012,
                            item_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=20021.38,
                                    marketplace_service_item_direct_flow_trans=20021.39,
                                    marketplace_service_item_dropoff_ff=20021.40,
                                    marketplace_service_item_dropoff_pvz=20021.41,
                                    marketplace_service_item_dropoff_sc=20021.42,
                                    marketplace_service_item_fulfillment=20021.43,
                                    marketplace_service_item_pickup=20021.44,
                                    marketplace_service_item_return_after_deliv_to_customer=20021.45,
                                    marketplace_service_item_return_flow_trans=20021.46,
                                    marketplace_service_item_return_not_deliv_to_customer=20021.47,
                                    marketplace_service_item_return_part_goods_customer=20021.48,
                                ),
                            old_price=20021.33,
                            payout=20021.34,
                            picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                amount=20021.49,
                                tag="tag #20022",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T23:04:05.999999+07:00",
                                ),
                            ),
                            price=20021.35,
                            product_id=20028023,
                            quantity=20028042,
                            total_discount_percent=20021.36,
                            total_discount_value=20021.37,
                        ),
                    ],
                ),
                is_express=True,
                order_id=200205,
                order_number="200212",
                posting_number="200223",
                products=[
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #2005", "mandatory mark #2006"],
                        name="name #20024",
                        offer_id="20025005",
                        price="20025012",
                        quantity=20025023,
                        sku=20025042,
                        currency_code="currency code #20021",
                    ),
                    posting_fbs_list.GetPostingFBSListResponseProduct(
                        mandatory_mark=["mandatory mark #2007", "mandatory mark #2008"],
                        name="name #20025",
                        offer_id="20026005",
                        price="20026012",
                        quantity=20026023,
                        sku=20026042,
                        currency_code="currency code #20022",
                    ),
                ],
                requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                    products_requiring_gtd=[29001, 29002],
                    products_requiring_country=[29003, 29004],
                    products_requiring_mandatory_mark=[29005, 29006],
                    products_requiring_rnpt=[29007, 29008],
                ),
                status="status #2002",
                tpl_integration_type="tpl integration type #2002",
                tracking_number="200242",
                delivering_date=datetime.datetime.fromisoformat(
                    "2006-01-03T15:04:05.999999+07:00",
                ),
                in_process_at=datetime.datetime.fromisoformat(
                    "2006-01-03T17:04:05.999999+07:00",
                ),
                shipment_date=datetime.datetime.fromisoformat(
                    "2006-01-03T19:04:05.999999+07:00",
                ),
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_package_label
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_package_label.get_posting_fbs_package_label,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_package_label.FBSPackageData(
            posting_number=["23", "42"],
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/package-label",
        response_cls=None,
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_package_label.get_posting_fbs_package_label,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_package_label.FBSPackageData(
            posting_number=["23", "42"],
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/package-label",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_list
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_list.get_posting_fbs_list,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_product_country_list
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_product_country_list.get_posting_fbs_product_country_list,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_product_country_list.CountryFilter(
            name_search="name",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/list",
        response_cls=posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_product_country_list.get_posting_fbs_product_country_list,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_product_country_list.CountryFilter(
            name_search="name",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/list",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_product_country_set
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_product_country_set.posting_fbs_product_country_set,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=posting_fbs_product_country_set.OderData(
            posting_number="23",
            product_id=42,
            country_iso_code="US",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/set",
        response_cls=posting_fbs_product_country_set.GetCountrySetFBSResponseResult,
    ),
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_product_country_set.posting_fbs_product_country_set,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=posting_fbs_product_country_set.OderData(
            posting_number="23",
            product_id=42,
            country_iso_code="US",
        ),
        expected_method="POST",
        expected_endpoint="/v2/posting/fbs/product/country/set",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # posting_fbs_ship_gtd
    IntegrationTestCase(
        kind="success",
        requester=posting_fbs_ship_gtd.create_posting_fbs_ship_with_gtd,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=posting_fbs_ship_gtd.create_posting_fbs_ship_with_gtd,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_description
    IntegrationTestCase(
        kind="success",
        requester=product_description.get_product_description,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=product_description.ProductData(
            offer_id="23",
            product_id=42,
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/info/description",
        response_cls=product_description.GetProductInfoDescriptionResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=product_description.get_product_description,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=product_description.ProductData(
            offer_id="23",
            product_id=42,
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/info/description",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_import_prices
    IntegrationTestCase(
        kind="success",
        requester=product_import_prices.set_product_import_price,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=product_import_prices.set_product_import_price,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_import_stocks
    IntegrationTestCase(
        kind="success",
        requester=product_import_stocks.set_stocks,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=product_import_stocks.set_stocks,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_info_attributes
    IntegrationTestCase(
        kind="success",
        requester=product_info_attributes.get_product_attributes,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=product_info_attributes.get_product_attributes_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=product_info_attributes.PaginatedProductFilter(
            filter=product_info_attributes.ProductFilter(
                offer_id=["105", "205"],
                product_id=["112", "212"],
                sku=["123", "223"],
                visibility=["one", "two"],
            ),
            last_id="",
            limit=2,
            sort_dir="sort-dir",
            sort_by="sort-by",
        ),
        expected_method="POST",
        expected_endpoint="/v4/product/info/attributes",
        response_cls=product_info_attributes.GetProductAttributesResponseResultWrapper,
        step_count=3,
        expected_response_items=[
            product_info_attributes.GetProductAttributesResponseResult(
                attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100100023,
                        complex_id=100100042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1001000023,
                                value="value #10011",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1002000023,
                                value="value #10012",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100200023,
                        complex_id=100200042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1003000023,
                                value="value #10013",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1004000023,
                                value="value #10014",
                            ),
                        ],
                    ),
                ],
                barcode="barcode #10011",
                barcodes=["barcode #1001", "barcode #1002"],
                description_category_id=1001005,
                color_image="color image #10011",
                complex_attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100300023,
                        complex_id=100300042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1005000023,
                                value="value #10015",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1006000023,
                                value="value #10016",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100400023,
                        complex_id=100400042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1007000023,
                                value="value #10017",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1008000023,
                                value="value #10018",
                            ),
                        ],
                    ),
                ],
                depth=1001012,
                dimension_unit="dimension unit #10011",
                height=1001023,
                id=1001042,
                images=["image #1001", "image #1002"],
                model_info=product_info_attributes.GetProductModelInfoValue(
                    model_id=10010023,
                    count=10010042,
                ),
                name="name #10011",
                offer_id="1002005",
                pdf_list=[
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #10011",
                        name="name #10012",
                    ),
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #10012",
                        name="name #10013",
                    ),
                ],
                primary_image="primary image #10011",
                sku=1002012,
                type_id=1002023,
                weight=1002042,
                weight_unit="weight unit #10011",
                width=1003005,
            ),
            product_info_attributes.GetProductAttributesResponseResult(
                attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100500023,
                        complex_id=100500042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=1009000023,
                                value="value #10021",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10010000023,
                                value="value #10022",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100600023,
                        complex_id=100600042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10011000023,
                                value="value #10023",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10012000023,
                                value="value #10024",
                            ),
                        ],
                    ),
                ],
                barcode="barcode #10021",
                barcodes=["barcode #1003", "barcode #1004"],
                description_category_id=1004005,
                color_image="color image #10021",
                complex_attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100700023,
                        complex_id=100700042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10013000023,
                                value="value #10025",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10014000023,
                                value="value #10026",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=100800023,
                        complex_id=100800042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10015000023,
                                value="value #10027",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=10016000023,
                                value="value #10028",
                            ),
                        ],
                    ),
                ],
                depth=1004012,
                dimension_unit="dimension unit #10021",
                height=1004023,
                id=1004042,
                images=["image #1003", "image #1004"],
                model_info=product_info_attributes.GetProductModelInfoValue(
                    model_id=10020023,
                    count=10020042,
                ),
                name="name #10021",
                offer_id="1005005",
                pdf_list=[
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #10021",
                        name="name #10022",
                    ),
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #10022",
                        name="name #10023",
                    ),
                ],
                primary_image="primary image #10021",
                sku=1005012,
                type_id=1005023,
                weight=1005042,
                weight_unit="weight unit #10021",
                width=1006005,
            ),
            product_info_attributes.GetProductAttributesResponseResult(
                attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200100023,
                        complex_id=200100042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2001000023,
                                value="value #20011",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2002000023,
                                value="value #20012",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200200023,
                        complex_id=200200042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2003000023,
                                value="value #20013",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2004000023,
                                value="value #20014",
                            ),
                        ],
                    ),
                ],
                barcode="barcode #20011",
                barcodes=["barcode #2001", "barcode #2002"],
                description_category_id=2001005,
                color_image="color image #20011",
                complex_attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200300023,
                        complex_id=200300042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2005000023,
                                value="value #20015",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2006000023,
                                value="value #20016",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200400023,
                        complex_id=200400042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2007000023,
                                value="value #20017",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2008000023,
                                value="value #20018",
                            ),
                        ],
                    ),
                ],
                depth=2001012,
                dimension_unit="dimension unit #20011",
                height=2001023,
                id=2001042,
                images=["image #2001", "image #2002"],
                model_info=product_info_attributes.GetProductModelInfoValue(
                    model_id=20010023,
                    count=20010042,
                ),
                name="name #20011",
                offer_id="2002005",
                pdf_list=[
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #20011",
                        name="name #20012",
                    ),
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #20012",
                        name="name #20013",
                    ),
                ],
                primary_image="primary image #20011",
                sku=2002012,
                type_id=2002023,
                weight=2002042,
                weight_unit="weight unit #20011",
                width=2003005,
            ),
            product_info_attributes.GetProductAttributesResponseResult(
                attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200500023,
                        complex_id=200500042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=2009000023,
                                value="value #20021",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20010000023,
                                value="value #20022",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200600023,
                        complex_id=200600042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20011000023,
                                value="value #20023",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20012000023,
                                value="value #20024",
                            ),
                        ],
                    ),
                ],
                barcode="barcode #20021",
                barcodes=["barcode #2003", "barcode #2004"],
                description_category_id=2004005,
                color_image="color image #20021",
                complex_attributes=[
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200700023,
                        complex_id=200700042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20013000023,
                                value="value #20025",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20014000023,
                                value="value #20026",
                            ),
                        ],
                    ),
                    product_info_attributes.GetProductAttributesResponseAttribute(
                        id=200800023,
                        complex_id=200800042,
                        values=[
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20015000023,
                                value="value #20027",
                            ),
                            product_info_attributes.GetProductAttributesDictionaryValue(
                                dictionary_value_id=20016000023,
                                value="value #20028",
                            ),
                        ],
                    ),
                ],
                depth=2004012,
                dimension_unit="dimension unit #20021",
                height=2004023,
                id=2004042,
                images=["image #2003", "image #2004"],
                model_info=product_info_attributes.GetProductModelInfoValue(
                    model_id=20020023,
                    count=20020042,
                ),
                name="name #20021",
                offer_id="2005005",
                pdf_list=[
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #20021",
                        name="name #20022",
                    ),
                    product_info_attributes.GetProductAttributesPdf(
                        file_name="file name #20022",
                        name="name #20023",
                    ),
                ],
                primary_image="primary image #20021",
                sku=2005012,
                type_id=2005023,
                weight=2005042,
                weight_unit="weight unit #20021",
                width=2006005,
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=product_info_attributes.get_product_attributes,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_info
    IntegrationTestCase(
        kind="success",
        requester=product_info.get_product_info,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=product_info.ProductData(
            offer_id="12",
            product_id=23,
            sku=42,
        ),
        expected_method="POST",
        expected_endpoint="/v2/product/info",
        response_cls=product_info.GetProductInfoResponseResultWrapper,
    ),
    IntegrationTestCase(
        kind="error",
        requester=product_info.get_product_info,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=product_info.ProductData(
            offer_id="12",
            product_id=23,
            sku=42,
        ),
        expected_method="POST",
        expected_endpoint="/v2/product/info",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # product_pictures_import
    IntegrationTestCase(
        kind="success",
        requester=product_pictures_import.send_product_pictures,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=product_pictures_import.send_product_pictures,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
        request_data=product_pictures_import.ProductPictures(
            color_image="color image",
            images=["image #1", "image #2"],
            images360=["images 360 #1", "images 360 #2"],
            product_id=23,
        ),
        expected_method="POST",
        expected_endpoint="/v1/product/pictures/import",
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # products_stocks
    IntegrationTestCase(
        kind="success",
        requester=products_stocks.set_stocks,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="error",
        requester=products_stocks.set_stocks,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # returns_fbo
    IntegrationTestCase(
        kind="success",
        requester=returns_fbo.get_returns_company_fbo,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=returns_fbo.get_returns_company_fbo_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=returns_fbo.PaginatedGetReturnsCompanyFBOFilter(
            filter=returns_fbo.GetReturnsCompanyFBOFilter(
                posting_number="12",
                status=["one", "two"],
            ),
            offset=0,
            limit=2,
        ),
        expected_method="POST",
        expected_endpoint="/v2/returns/company/fbo",
        response_cls=returns_fbo.GetReturnsCompanyFBOResponseResult,
        step_count=3,
        expected_response_items=[
            returns_fbo.GetReturnsCompanyFBOResponseItem(
                company_id=105,
                current_place_name="current place name #1",
                dst_place_name="dst place name #1",
                id=112,
                is_opened=True,
                posting_number="123",
                return_reason_name="return reason name #1",
                sku=142,
                status_name="status name #1",
                accepted_from_customer_moment=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
                returned_to_ozon_moment=datetime.datetime.fromisoformat(
                    "2006-01-02T17:04:05.999999+07:00",
                ),
            ),
            returns_fbo.GetReturnsCompanyFBOResponseItem(
                company_id=205,
                current_place_name="current place name #2",
                dst_place_name="dst place name #2",
                id=212,
                is_opened=True,
                posting_number="223",
                return_reason_name="return reason name #2",
                sku=242,
                status_name="status name #2",
                accepted_from_customer_moment=datetime.datetime.fromisoformat(
                    "2006-01-02T19:04:05.999999+07:00",
                ),
                returned_to_ozon_moment=datetime.datetime.fromisoformat(
                    "2006-01-02T21:04:05.999999+07:00",
                ),
            ),
            returns_fbo.GetReturnsCompanyFBOResponseItem(
                company_id=305,
                current_place_name="current place name #3",
                dst_place_name="dst place name #3",
                id=312,
                is_opened=True,
                posting_number="323",
                return_reason_name="return reason name #3",
                sku=342,
                status_name="status name #3",
                accepted_from_customer_moment=datetime.datetime.fromisoformat(
                    "2006-01-03T15:04:05.999999+07:00",
                ),
                returned_to_ozon_moment=datetime.datetime.fromisoformat(
                    "2006-01-03T17:04:05.999999+07:00",
                ),
            ),
            returns_fbo.GetReturnsCompanyFBOResponseItem(
                company_id=405,
                current_place_name="current place name #4",
                dst_place_name="dst place name #4",
                id=412,
                is_opened=True,
                posting_number="423",
                return_reason_name="return reason name #4",
                sku=442,
                status_name="status name #4",
                accepted_from_customer_moment=datetime.datetime.fromisoformat(
                    "2006-01-03T19:04:05.999999+07:00",
                ),
                returned_to_ozon_moment=datetime.datetime.fromisoformat(
                    "2006-01-03T21:04:05.999999+07:00",
                ),
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=returns_fbo.get_returns_company_fbo,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # returns_fbs
    IntegrationTestCase(
        kind="success",
        requester=returns_fbs.get_returns_company_fbs,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=returns_fbs.get_returns_company_fbs_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
            offset=0,
            limit=2,
        ),
        expected_method="POST",
        expected_endpoint="/v2/returns/company/fbs",
        response_cls=returns_fbs.GetReturnsCompanyFBSResponseResultWrapper,
        step_count=3,
        expected_response_items=[
            returns_fbs.GetReturnsCompanyFBSResponseItem(
                accepted_from_customer_moment="accepted from customer moment #1",
                clearing_id=101,
                commission=102.5,
                commission_percent=53.5,
                id=104,
                is_moving=True,
                is_opened=True,
                last_free_waiting_day="last free waiting day #1",
                place_id=105,
                moving_to_place_name="moving to place name #1",
                picking_amount=106.5,
                posting_number="107",
                price=108.5,
                price_without_commission=109.5,
                product_id=110,
                product_name="product name #1",
                quantity=111,
                return_date="2006-01-02T08:04:05.999999+00:00",
                return_reason_name="return reason name #1",
                waiting_for_seller_date_time="2006-01-02T10:04:05.999999+00:00",
                returned_to_seller_date_time="2006-01-02T12:04:05.999999+00:00",
                waiting_for_seller_days=112,
                returns_keeping_cost=113.5,
                sku=114,
                status="status #1",
            ),
            returns_fbs.GetReturnsCompanyFBSResponseItem(
                accepted_from_customer_moment="accepted from customer moment #2",
                clearing_id=201,
                commission=202.5,
                commission_percent=73.5,
                id=204,
                is_moving=True,
                is_opened=True,
                last_free_waiting_day="last free waiting day #2",
                place_id=205,
                moving_to_place_name="moving to place name #2",
                picking_amount=206.5,
                posting_number="207",
                price=208.5,
                price_without_commission=209.5,
                product_id=210,
                product_name="product name #2",
                quantity=211,
                return_date="2006-01-02T14:04:05.999999+00:00",
                return_reason_name="return reason name #2",
                waiting_for_seller_date_time="2006-01-02T16:04:05.999999+00:00",
                returned_to_seller_date_time="2006-01-02T18:04:05.999999+00:00",
                waiting_for_seller_days=212,
                returns_keeping_cost=213.5,
                sku=214,
                status="status #2",
            ),
            returns_fbs.GetReturnsCompanyFBSResponseItem(
                accepted_from_customer_moment="accepted from customer moment #3",
                clearing_id=301,
                commission=302.5,
                commission_percent=53.5,
                id=304,
                is_moving=True,
                is_opened=True,
                last_free_waiting_day="last free waiting day #3",
                place_id=305,
                moving_to_place_name="moving to place name #3",
                picking_amount=306.5,
                posting_number="307",
                price=308.5,
                price_without_commission=309.5,
                product_id=310,
                product_name="product name #3",
                quantity=311,
                return_date="2006-01-02T08:04:05.999999+00:00",
                return_reason_name="return reason name #3",
                waiting_for_seller_date_time="2006-01-03T10:04:05.999999+00:00",
                returned_to_seller_date_time="2006-01-03T12:04:05.999999+00:00",
                waiting_for_seller_days=312,
                returns_keeping_cost=313.5,
                sku=314,
                status="status #3",
            ),
            returns_fbs.GetReturnsCompanyFBSResponseItem(
                accepted_from_customer_moment="accepted from customer moment #4",
                clearing_id=401,
                commission=402.5,
                commission_percent=73.5,
                id=404,
                is_moving=True,
                is_opened=True,
                last_free_waiting_day="last free waiting day #4",
                place_id=405,
                moving_to_place_name="moving to place name #4",
                picking_amount=406.5,
                posting_number="407",
                price=408.5,
                price_without_commission=409.5,
                product_id=410,
                product_name="product name #4",
                quantity=411,
                return_date="2006-01-02T14:04:05.999999+00:00",
                return_reason_name="return reason name #4",
                waiting_for_seller_date_time="2006-01-03T16:04:05.999999+00:00",
                returned_to_seller_date_time="2006-01-03T18:04:05.999999+00:00",
                waiting_for_seller_days=412,
                returns_keeping_cost=413.5,
                sku=414,
                status="status #4",
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=returns_fbs.get_returns_company_fbs,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),

    # stocks
    IntegrationTestCase(
        kind="success",
        requester=stocks.get_product_info_stocks,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
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
    IntegrationTestCase(
        kind="iterative",
        requester=stocks.get_product_info_stocks_iterative,
        request_credentials=common.TEST_EXPECTED_CREDENTIALS,
        request_data=stocks.PaginatedProductFilter(
            filter=stocks.ProductFilter(
                offer_id=["105", "205"],
                product_id=["112", "212"],
                visibility="visibility",
                with_quant=stocks.ProductFilterWithQuant(
                    created=True,
                ),
            ),
            cursor="",
            limit=2,
        ),
        expected_method="POST",
        expected_endpoint="/v4/product/info/stocks",
        response_cls=stocks.GetProductInfoStocksResponseResult,
        step_count=3,
        expected_response_items=[
            stocks.GetProductInfoStocksResponseItem(
                offer_id="123",
                product_id=142,
                stocks=[
                    stocks.GetProductInfoStocksResponseStock(
                        present=1023,
                        reserved=1042,
                        type="type #1",
                    ),
                    stocks.GetProductInfoStocksResponseStock(
                        present=2023,
                        reserved=2042,
                        type="type #2",
                    ),
                ],
            ),
            stocks.GetProductInfoStocksResponseItem(
                offer_id="223",
                product_id=242,
                stocks=[
                    stocks.GetProductInfoStocksResponseStock(
                        present=3023,
                        reserved=3042,
                        type="type #3",
                    ),
                    stocks.GetProductInfoStocksResponseStock(
                        present=4023,
                        reserved=4042,
                        type="type #4",
                    ),
                ],
            ),
            stocks.GetProductInfoStocksResponseItem(
                offer_id="323",
                product_id=342,
                stocks=[
                    stocks.GetProductInfoStocksResponseStock(
                        present=5023,
                        reserved=5042,
                        type="type #5",
                    ),
                    stocks.GetProductInfoStocksResponseStock(
                        present=6023,
                        reserved=6042,
                        type="type #6",
                    ),
                ],
            ),
            stocks.GetProductInfoStocksResponseItem(
                offer_id="423",
                product_id=442,
                stocks=[
                    stocks.GetProductInfoStocksResponseStock(
                        present=7023,
                        reserved=7042,
                        type="type #7",
                    ),
                    stocks.GetProductInfoStocksResponseStock(
                        present=8023,
                        reserved=8042,
                        type="type #8",
                    ),
                ],
            ),
        ],
    ),
    IntegrationTestCase(
        kind="error",
        requester=stocks.get_product_info_stocks,
        request_credentials=common.TEST_INVALID_CREDENTIALS,
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
        expected_exception=_TEST_HTTP_ERROR,
    ),
]


class TestIntegration(unittest.TestCase):
    def test_integration(self) -> None:
        for test_case in _INTEGRATION_TEST_CASES:
            with self.subTest(test_case.name):
                test_case.validate_modules()
                test_case.validate_iterative_mode()

                endpoints = [
                    test_case.make_endpoint(step_index)
                    for step_index in range(test_case.step_count)
                ]

                expected_response = test_case.make_expected_response(endpoints)

                with TestServer(endpoints) as server:
                    request_api._API_BASE_URL = server.address

                    if test_case.expected_exception is not None:
                        with self.assertRaises(http_error.HTTPError) as actual_exception_catcher:
                            test_case.call_requester()

                        self.assertEqual(
                            test_case.expected_exception,
                            actual_exception_catcher.exception,
                        )
                    else:
                        actual_response = test_case.call_requester()

                        self.assertEqual(expected_response, actual_response)
