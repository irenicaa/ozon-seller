from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
import pathlib
import unittest
import datetime

from . import common
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
    posting_fbs_get,
    posting_fbs_list,
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
class _ResponseTestCase:
    kind: str
    expected_data: DataClassJsonMixin


_TEST_DATA_PATH = pathlib.Path(__file__).parent.joinpath(common.TEST_DATA_DIRECTORY)
_RESPONSES_TEST_CASES: list[_ResponseTestCase] = [
    # actions_candidates.GetActionsCandidatesResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=actions_candidates.GetActionsCandidatesResponseResultWrapper(
            result=actions_candidates.GetActionsCandidatesResponseResult(
                products=[],
                total=0.0,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=actions_candidates.GetActionsCandidatesResponseResultWrapper(
            result=actions_candidates.GetActionsCandidatesResponseResult(
                products=[
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
                ],
                total=100.0,
            ),
        ),
    ),

    # actions_products.GetSellerProductResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=actions_products.GetSellerProductResponseResultWrapper(
            result=actions_products.GetSellerProductResponseResult(
                products=[],
                total=0,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=actions_products.GetSellerProductResponseResultWrapper(
            result=actions_products.GetSellerProductResponseResult(
                products=[
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
                ],
                total=100,
            ),
        ),
    ),

    # actions.GetSellerActionsResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=actions.GetSellerActionsResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=actions.GetSellerActionsResponseResultWrapper(
            result=[
                actions.GetSellerActionsResponseResult(
                    id=100.5,
                    title="title #1",
                    action_type="action type #1",
                    description="description #1",
                    date_start="2006-01-02T08:04:05.999999+00:00",
                    date_end="2006-01-02T10:04:05.999999+00:00",
                    freeze_date="2006-01-02T12:04:05.999999+00:00",
                    potential_products_count=101.2,
                    participating_products_count=102.3,
                    is_participating=True,
                    banned_products_count=104.2,
                    with_targeting=True,
                    order_amount=150.5,
                    discount_type="discount type #1",
                    discount_value=151.2,
                    is_voucher_action=True,
                ),
                actions.GetSellerActionsResponseResult(
                    id=200.5,
                    title="title #2",
                    action_type="action type #2",
                    description="description #2",
                    date_start="2006-01-02T14:04:05.999999+00:00",
                    date_end="2006-01-02T16:04:05.999999+00:00",
                    freeze_date="2006-01-02T18:04:05.999999+00:00",
                    potential_products_count=201.2,
                    participating_products_count=202.3,
                    is_participating=True,
                    banned_products_count=204.2,
                    with_targeting=True,
                    order_amount=250.5,
                    discount_type="discount type #2",
                    discount_value=251.2,
                    is_voucher_action=True,
                ),
            ],
        ),
    ),

    # chat_send_message.GetChatStartResponseResult
    _ResponseTestCase(
        kind="full",
        expected_data=chat_send_message.GetChatStartResponseResult(
            result="result",
        ),
    ),

    # chat_start.GetChatStartResponseResultWrapper
    _ResponseTestCase(
        kind="full",
        expected_data=chat_start.GetChatStartResponseResultWrapper(
            result=chat_start.GetChatStartResponseResult(
                chat_id="23",
            ),
        ),
    ),

    # fbs_act_get_postings.PostingFBSActDataResponseResultWrapper
    _ResponseTestCase(
        kind="top_level_empty_list",
        expected_data=fbs_act_get_postings.PostingFBSActDataResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=fbs_act_get_postings.PostingFBSActDataResponseResultWrapper(
            result=[
                fbs_act_get_postings.PostingFBSActDataResponseResult(
                    id=112,
                    multi_box_qty=123,
                    posting_number="142",
                    status="status #1",
                    seller_error="seller error #1",
                    updated_at="2006-01-02T17:04:05.999999+07:00",
                    created_at="2006-01-02T15:04:05.999999+07:00",
                    products=[],
                ),
                fbs_act_get_postings.PostingFBSActDataResponseResult(
                    id=212,
                    multi_box_qty=223,
                    posting_number="242",
                    status="status #2",
                    seller_error="seller error #2",
                    updated_at="2006-01-03T17:04:05.999999+07:00",
                    created_at="2006-01-03T15:04:05.999999+07:00",
                    products=[],
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=fbs_act_get_postings.PostingFBSActDataResponseResultWrapper(
            result=[
                fbs_act_get_postings.PostingFBSActDataResponseResult(
                    id=112,
                    multi_box_qty=123,
                    posting_number="142",
                    status="status #1",
                    seller_error="seller error #1",
                    updated_at="2006-01-02T17:04:05.999999+07:00",
                    created_at="2006-01-02T15:04:05.999999+07:00",
                    products=[
                        fbs_act_get_postings.PostingFBSActDataResponseProducts(
                            name="name #1",
                            offer_id="1005",
                            price="1012.5",
                            quantity=1023,
                            sku=1042,
                        ),
                        fbs_act_get_postings.PostingFBSActDataResponseProducts(
                            name="name #2",
                            offer_id="2005",
                            price="2012.5",
                            quantity=2023,
                            sku=2042,
                        ),
                    ],
                ),
                fbs_act_get_postings.PostingFBSActDataResponseResult(
                    id=212,
                    multi_box_qty=223,
                    posting_number="242",
                    status="status #2",
                    seller_error="seller error #2",
                    updated_at="2006-01-03T17:04:05.999999+07:00",
                    created_at="2006-01-03T15:04:05.999999+07:00",
                    products=[
                        fbs_act_get_postings.PostingFBSActDataResponseProducts(
                            name="name #3",
                            offer_id="3005",
                            price="3012.5",
                            quantity=3023,
                            sku=3042,
                        ),
                        fbs_act_get_postings.PostingFBSActDataResponseProducts(
                            name="name #4",
                            offer_id="4005",
                            price="4012.5",
                            quantity=4023,
                            sku=4042,
                        ),
                    ],
                ),
            ],
        ),
    ),

    # posting_fbo_list.GetPostingFBOListResponseResultWrapper
    _ResponseTestCase(
        kind="top_level_empty_list",
        expected_data=posting_fbo_list.GetPostingFBOListResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=posting_fbo_list.GetPostingFBOListResponseResultWrapper(
            result=[
                posting_fbo_list.GetPostingFBOListResponseResult(
                    additional_data=[],
                    analytics_data=None,
                    cancel_reason_id=105,
                    financial_data=None,
                    order_id=112,
                    order_number="123",
                    posting_number="142",
                    products=[],
                    status="status #1",
                    created_at=None,
                    in_process_at=None,
                ),
                posting_fbo_list.GetPostingFBOListResponseResult(
                    additional_data=[],
                    analytics_data=None,
                    cancel_reason_id=205,
                    financial_data=None,
                    order_id=212,
                    order_number="223",
                    posting_number="242",
                    products=[],
                    status="status #2",
                    created_at=None,
                    in_process_at=None,
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty_list",
        expected_data=posting_fbo_list.GetPostingFBOListResponseResultWrapper(
            result=[
                posting_fbo_list.GetPostingFBOListResponseResult(
                    additional_data=[
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #1",
                            value="value #1",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #2",
                            value="value #2",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #1",
                        delivery_type="delivery type #1",
                        is_legal=False,
                        is_premium=False,
                        payment_type_group_name="payment type group name #1",
                        region="region #1",
                        warehouse_id=1023,
                        warehouse_name="warehouse name #1",
                    ),
                    cancel_reason_id=105,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=1.01,
                                marketplace_service_item_direct_flow_trans=1.02,
                                marketplace_service_item_dropoff_ff=1.03,
                                marketplace_service_item_dropoff_pvz=1.04,
                                marketplace_service_item_dropoff_sc=1.05,
                                marketplace_service_item_fulfillment=1.06,
                                marketplace_service_item_pickup=1.07,
                                marketplace_service_item_return_after_deliv_to_customer=1.08,
                                marketplace_service_item_return_flow_trans=1.09,
                                marketplace_service_item_return_not_deliv_to_customer=1.10,
                                marketplace_service_item_return_part_goods_customer=1.11,
                            ),
                        products=[],
                    ),
                    order_id=112,
                    order_number="123",
                    posting_number="142",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=[],
                            name="name #1",
                            offer_id="10005",
                            price="10012",
                            quantity=10023,
                            sku=10042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=[],
                            name="name #2",
                            offer_id="20005",
                            price="20012",
                            quantity=20023,
                            sku=20042,
                        ),
                    ],
                    status="status #1",
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
                            key="key #3",
                            value="value #3",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #4",
                            value="value #4",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #2",
                        delivery_type="delivery type #2",
                        is_legal=True,
                        is_premium=True,
                        payment_type_group_name="payment type group name #2",
                        region="region #2",
                        warehouse_id=2023,
                        warehouse_name="warehouse name #2",
                    ),
                    cancel_reason_id=205,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=2.01,
                                marketplace_service_item_direct_flow_trans=2.02,
                                marketplace_service_item_dropoff_ff=2.03,
                                marketplace_service_item_dropoff_pvz=2.04,
                                marketplace_service_item_dropoff_sc=2.05,
                                marketplace_service_item_fulfillment=2.06,
                                marketplace_service_item_pickup=2.07,
                                marketplace_service_item_return_after_deliv_to_customer=2.08,
                                marketplace_service_item_return_flow_trans=2.09,
                                marketplace_service_item_return_not_deliv_to_customer=2.10,
                                marketplace_service_item_return_part_goods_customer=2.11,
                            ),
                        products=[],
                    ),
                    order_id=212,
                    order_number="223",
                    posting_number="242",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=[],
                            name="name #3",
                            offer_id="30005",
                            price="30012",
                            quantity=30023,
                            sku=30042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=[],
                            name="name #4",
                            offer_id="40005",
                            price="40012",
                            quantity=40023,
                            sku=40042,
                        ),
                    ],
                    status="status #2",
                    created_at=datetime.datetime.fromisoformat(
                        "2006-01-03T15:04:05.999999+07:00",
                    ),
                    in_process_at=datetime.datetime.fromisoformat(
                        "2006-01-03T17:04:05.999999+07:00",
                    ),
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="fourth_level_empty_list",
        expected_data=posting_fbo_list.GetPostingFBOListResponseResultWrapper(
            result=[
                posting_fbo_list.GetPostingFBOListResponseResult(
                    additional_data=[
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #1",
                            value="value #1",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #2",
                            value="value #2",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #1",
                        delivery_type="delivery type #1",
                        is_legal=False,
                        is_premium=False,
                        payment_type_group_name="payment type group name #1",
                        region="region #1",
                        warehouse_id=1023,
                        warehouse_name="warehouse name #1",
                    ),
                    cancel_reason_id=105,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=1.01,
                                marketplace_service_item_direct_flow_trans=1.02,
                                marketplace_service_item_dropoff_ff=1.03,
                                marketplace_service_item_dropoff_pvz=1.04,
                                marketplace_service_item_dropoff_sc=1.05,
                                marketplace_service_item_fulfillment=1.06,
                                marketplace_service_item_pickup=1.07,
                                marketplace_service_item_return_after_deliv_to_customer=1.08,
                                marketplace_service_item_return_flow_trans=1.09,
                                marketplace_service_item_return_not_deliv_to_customer=1.10,
                                marketplace_service_item_return_part_goods_customer=1.11,
                            ),
                        products=[
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=[],
                                client_price="100005",
                                commission_amount=10.01,
                                commission_percent=100012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=100.01,
                                        marketplace_service_item_direct_flow_trans=100.02,
                                        marketplace_service_item_dropoff_ff=100.03,
                                        marketplace_service_item_dropoff_pvz=100.04,
                                        marketplace_service_item_dropoff_sc=100.05,
                                        marketplace_service_item_fulfillment=100.06,
                                        marketplace_service_item_pickup=100.07,
                                        marketplace_service_item_return_after_deliv_to_customer=100.08,
                                        marketplace_service_item_return_flow_trans=100.09,
                                        marketplace_service_item_return_not_deliv_to_customer=100.10,
                                        marketplace_service_item_return_part_goods_customer=100.11,
                                    ),
                                old_price=10.02,
                                payout=10.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=100.12,
                                    tag="tag #1",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-02T19:04:05.999999+07:00",
                                    ),
                                ),
                                price=10.04,
                                product_id=100023,
                                quantity=100042,
                                total_discount_percent=10.05,
                                total_discount_value=10.06,
                            ),
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=[],
                                client_price="200005",
                                commission_amount=20.01,
                                commission_percent=200012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=200.01,
                                        marketplace_service_item_direct_flow_trans=200.02,
                                        marketplace_service_item_dropoff_ff=200.03,
                                        marketplace_service_item_dropoff_pvz=200.04,
                                        marketplace_service_item_dropoff_sc=200.05,
                                        marketplace_service_item_fulfillment=200.06,
                                        marketplace_service_item_pickup=200.07,
                                        marketplace_service_item_return_after_deliv_to_customer=200.08,
                                        marketplace_service_item_return_flow_trans=200.09,
                                        marketplace_service_item_return_not_deliv_to_customer=200.10,
                                        marketplace_service_item_return_part_goods_customer=200.11,
                                    ),
                                old_price=20.02,
                                payout=20.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=200.12,
                                    tag="tag #2",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-02T21:04:05.999999+07:00",
                                    ),
                                ),
                                price=20.04,
                                product_id=200023,
                                quantity=200042,
                                total_discount_percent=20.05,
                                total_discount_value=20.06,
                            ),
                        ],
                    ),
                    order_id=112,
                    order_number="123",
                    posting_number="142",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #1", "digital code #2"],
                            name="name #1",
                            offer_id="10005",
                            price="10012",
                            quantity=10023,
                            sku=10042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #3", "digital code #4"],
                            name="name #2",
                            offer_id="20005",
                            price="20012",
                            quantity=20023,
                            sku=20042,
                        ),
                    ],
                    status="status #1",
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
                            key="key #3",
                            value="value #3",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #4",
                            value="value #4",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #2",
                        delivery_type="delivery type #2",
                        is_legal=True,
                        is_premium=True,
                        payment_type_group_name="payment type group name #2",
                        region="region #2",
                        warehouse_id=2023,
                        warehouse_name="warehouse name #2",
                    ),
                    cancel_reason_id=205,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=2.01,
                                marketplace_service_item_direct_flow_trans=2.02,
                                marketplace_service_item_dropoff_ff=2.03,
                                marketplace_service_item_dropoff_pvz=2.04,
                                marketplace_service_item_dropoff_sc=2.05,
                                marketplace_service_item_fulfillment=2.06,
                                marketplace_service_item_pickup=2.07,
                                marketplace_service_item_return_after_deliv_to_customer=2.08,
                                marketplace_service_item_return_flow_trans=2.09,
                                marketplace_service_item_return_not_deliv_to_customer=2.10,
                                marketplace_service_item_return_part_goods_customer=2.11,
                            ),
                        products=[
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=[],
                                client_price="300005",
                                commission_amount=30.01,
                                commission_percent=300012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=300.01,
                                        marketplace_service_item_direct_flow_trans=300.02,
                                        marketplace_service_item_dropoff_ff=300.03,
                                        marketplace_service_item_dropoff_pvz=300.04,
                                        marketplace_service_item_dropoff_sc=300.05,
                                        marketplace_service_item_fulfillment=300.06,
                                        marketplace_service_item_pickup=300.07,
                                        marketplace_service_item_return_after_deliv_to_customer=300.08,
                                        marketplace_service_item_return_flow_trans=300.09,
                                        marketplace_service_item_return_not_deliv_to_customer=300.10,
                                        marketplace_service_item_return_part_goods_customer=300.11,
                                    ),
                                old_price=30.02,
                                payout=30.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=300.12,
                                    tag="tag #1",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-03T19:04:05.999999+07:00",
                                    ),
                                ),
                                price=30.04,
                                product_id=300023,
                                quantity=300042,
                                total_discount_percent=30.05,
                                total_discount_value=30.06,
                            ),
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=[],
                                client_price="400005",
                                commission_amount=40.01,
                                commission_percent=400012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=400.01,
                                        marketplace_service_item_direct_flow_trans=400.02,
                                        marketplace_service_item_dropoff_ff=400.03,
                                        marketplace_service_item_dropoff_pvz=400.04,
                                        marketplace_service_item_dropoff_sc=400.05,
                                        marketplace_service_item_fulfillment=400.06,
                                        marketplace_service_item_pickup=400.07,
                                        marketplace_service_item_return_after_deliv_to_customer=400.08,
                                        marketplace_service_item_return_flow_trans=400.09,
                                        marketplace_service_item_return_not_deliv_to_customer=400.10,
                                        marketplace_service_item_return_part_goods_customer=400.11,
                                    ),
                                old_price=40.02,
                                payout=40.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=400.12,
                                    tag="tag #2",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-03T21:04:05.999999+07:00",
                                    ),
                                ),
                                price=40.04,
                                product_id=400023,
                                quantity=400042,
                                total_discount_percent=40.05,
                                total_discount_value=40.06,
                            ),
                        ],
                    ),
                    order_id=212,
                    order_number="223",
                    posting_number="242",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #5", "digital code #6"],
                            name="name #3",
                            offer_id="30005",
                            price="30012",
                            quantity=30023,
                            sku=30042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #7", "digital code #8"],
                            name="name #4",
                            offer_id="40005",
                            price="40012",
                            quantity=40023,
                            sku=40042,
                        ),
                    ],
                    status="status #2",
                    created_at=datetime.datetime.fromisoformat(
                        "2006-01-03T15:04:05.999999+07:00",
                    ),
                    in_process_at=datetime.datetime.fromisoformat(
                        "2006-01-03T17:04:05.999999+07:00",
                    ),
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbo_list.GetPostingFBOListResponseResultWrapper(
            result=[
                posting_fbo_list.GetPostingFBOListResponseResult(
                    additional_data=[
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #1",
                            value="value #1",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #2",
                            value="value #2",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #1",
                        delivery_type="delivery type #1",
                        is_legal=False,
                        is_premium=False,
                        payment_type_group_name="payment type group name #1",
                        region="region #1",
                        warehouse_id=1023,
                        warehouse_name="warehouse name #1",
                    ),
                    cancel_reason_id=105,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=1.01,
                                marketplace_service_item_direct_flow_trans=1.02,
                                marketplace_service_item_dropoff_ff=1.03,
                                marketplace_service_item_dropoff_pvz=1.04,
                                marketplace_service_item_dropoff_sc=1.05,
                                marketplace_service_item_fulfillment=1.06,
                                marketplace_service_item_pickup=1.07,
                                marketplace_service_item_return_after_deliv_to_customer=1.08,
                                marketplace_service_item_return_flow_trans=1.09,
                                marketplace_service_item_return_not_deliv_to_customer=1.10,
                                marketplace_service_item_return_part_goods_customer=1.11,
                            ),
                        products=[
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=["action #1", "action #2"],
                                client_price="100005",
                                commission_amount=10.01,
                                commission_percent=100012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=100.01,
                                        marketplace_service_item_direct_flow_trans=100.02,
                                        marketplace_service_item_dropoff_ff=100.03,
                                        marketplace_service_item_dropoff_pvz=100.04,
                                        marketplace_service_item_dropoff_sc=100.05,
                                        marketplace_service_item_fulfillment=100.06,
                                        marketplace_service_item_pickup=100.07,
                                        marketplace_service_item_return_after_deliv_to_customer=100.08,
                                        marketplace_service_item_return_flow_trans=100.09,
                                        marketplace_service_item_return_not_deliv_to_customer=100.10,
                                        marketplace_service_item_return_part_goods_customer=100.11,
                                    ),
                                old_price=10.02,
                                payout=10.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=100.12,
                                    tag="tag #1",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-02T19:04:05.999999+07:00",
                                    ),
                                ),
                                price=10.04,
                                product_id=100023,
                                quantity=100042,
                                total_discount_percent=10.05,
                                total_discount_value=10.06,
                            ),
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=["action #3", "action #4"],
                                client_price="200005",
                                commission_amount=20.01,
                                commission_percent=200012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=200.01,
                                        marketplace_service_item_direct_flow_trans=200.02,
                                        marketplace_service_item_dropoff_ff=200.03,
                                        marketplace_service_item_dropoff_pvz=200.04,
                                        marketplace_service_item_dropoff_sc=200.05,
                                        marketplace_service_item_fulfillment=200.06,
                                        marketplace_service_item_pickup=200.07,
                                        marketplace_service_item_return_after_deliv_to_customer=200.08,
                                        marketplace_service_item_return_flow_trans=200.09,
                                        marketplace_service_item_return_not_deliv_to_customer=200.10,
                                        marketplace_service_item_return_part_goods_customer=200.11,
                                    ),
                                old_price=20.02,
                                payout=20.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=200.12,
                                    tag="tag #2",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-02T21:04:05.999999+07:00",
                                    ),
                                ),
                                price=20.04,
                                product_id=200023,
                                quantity=200042,
                                total_discount_percent=20.05,
                                total_discount_value=20.06,
                            ),
                        ],
                    ),
                    order_id=112,
                    order_number="123",
                    posting_number="142",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #1", "digital code #2"],
                            name="name #1",
                            offer_id="10005",
                            price="10012",
                            quantity=10023,
                            sku=10042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #3", "digital code #4"],
                            name="name #2",
                            offer_id="20005",
                            price="20012",
                            quantity=20023,
                            sku=20042,
                        ),
                    ],
                    status="status #1",
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
                            key="key #3",
                            value="value #3",
                        ),
                        posting_fbo_list.GetPostingFBOAdditionalDataItem(
                            key="key #4",
                            value="value #4",
                        ),
                    ],
                    analytics_data=posting_fbo_list.GetPostingFBOListResponseAnalyticsData(
                        city="city #2",
                        delivery_type="delivery type #2",
                        is_legal=True,
                        is_premium=True,
                        payment_type_group_name="payment type group name #2",
                        region="region #2",
                        warehouse_id=2023,
                        warehouse_name="warehouse name #2",
                    ),
                    cancel_reason_id=205,
                    financial_data=posting_fbo_list.GetPostingFBOListResponseFinancialData(
                        posting_services=\
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=2.01,
                                marketplace_service_item_direct_flow_trans=2.02,
                                marketplace_service_item_dropoff_ff=2.03,
                                marketplace_service_item_dropoff_pvz=2.04,
                                marketplace_service_item_dropoff_sc=2.05,
                                marketplace_service_item_fulfillment=2.06,
                                marketplace_service_item_pickup=2.07,
                                marketplace_service_item_return_after_deliv_to_customer=2.08,
                                marketplace_service_item_return_flow_trans=2.09,
                                marketplace_service_item_return_not_deliv_to_customer=2.10,
                                marketplace_service_item_return_part_goods_customer=2.11,
                            ),
                        products=[
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=["action #5", "action #6"],
                                client_price="300005",
                                commission_amount=30.01,
                                commission_percent=300012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=300.01,
                                        marketplace_service_item_direct_flow_trans=300.02,
                                        marketplace_service_item_dropoff_ff=300.03,
                                        marketplace_service_item_dropoff_pvz=300.04,
                                        marketplace_service_item_dropoff_sc=300.05,
                                        marketplace_service_item_fulfillment=300.06,
                                        marketplace_service_item_pickup=300.07,
                                        marketplace_service_item_return_after_deliv_to_customer=300.08,
                                        marketplace_service_item_return_flow_trans=300.09,
                                        marketplace_service_item_return_not_deliv_to_customer=300.10,
                                        marketplace_service_item_return_part_goods_customer=300.11,
                                    ),
                                old_price=30.02,
                                payout=30.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=300.12,
                                    tag="tag #1",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-03T19:04:05.999999+07:00",
                                    ),
                                ),
                                price=30.04,
                                product_id=300023,
                                quantity=300042,
                                total_discount_percent=30.05,
                                total_discount_value=30.06,
                            ),
                            posting_fbo_list.GetPostingFBOListResponseFinancialDataProduct(
                                actions=["action #7", "action #8"],
                                client_price="400005",
                                commission_amount=40.01,
                                commission_percent=400012,
                                item_services=\
                                    posting_fbo_list.GetPostingFBOListResponseFinancialDataServices(
                                        marketplace_service_item_deliv_to_customer=400.01,
                                        marketplace_service_item_direct_flow_trans=400.02,
                                        marketplace_service_item_dropoff_ff=400.03,
                                        marketplace_service_item_dropoff_pvz=400.04,
                                        marketplace_service_item_dropoff_sc=400.05,
                                        marketplace_service_item_fulfillment=400.06,
                                        marketplace_service_item_pickup=400.07,
                                        marketplace_service_item_return_after_deliv_to_customer=400.08,
                                        marketplace_service_item_return_flow_trans=400.09,
                                        marketplace_service_item_return_not_deliv_to_customer=400.10,
                                        marketplace_service_item_return_part_goods_customer=400.11,
                                    ),
                                old_price=40.02,
                                payout=40.03,
                                picking=posting_fbo_list.GetPostingFBOListResponsePicking(
                                    amount=400.12,
                                    tag="tag #2",
                                    moment=datetime.datetime.fromisoformat(
                                        "2006-01-03T21:04:05.999999+07:00",
                                    ),
                                ),
                                price=40.04,
                                product_id=400023,
                                quantity=400042,
                                total_discount_percent=40.05,
                                total_discount_value=40.06,
                            ),
                        ],
                    ),
                    order_id=212,
                    order_number="223",
                    posting_number="242",
                    products=[
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #5", "digital code #6"],
                            name="name #3",
                            offer_id="30005",
                            price="30012",
                            quantity=30023,
                            sku=30042,
                        ),
                        posting_fbo_list.GetPostingFBOListResponseProduct(
                            digital_codes=["digital code #7", "digital code #8"],
                            name="name #4",
                            offer_id="40005",
                            price="40012",
                            quantity=40023,
                            sku=40042,
                        ),
                    ],
                    status="status #2",
                    created_at=datetime.datetime.fromisoformat(
                        "2006-01-03T15:04:05.999999+07:00",
                    ),
                    in_process_at=datetime.datetime.fromisoformat(
                        "2006-01-03T17:04:05.999999+07:00",
                    ),
                ),
            ],
        ),
    ),

    # posting_fbs_act_check_status.PostingFBSActCreateResponseActResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=posting_fbs_act_check_status.PostingFBSActCreateResponseActResultWrapper(
            result=posting_fbs_act_check_status.PostingFBSActCheckStatusResponseResult(
                act_type="act_type",
                added_to_act=[],
                removed_from_act=[],
                status="status",
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_act_check_status.PostingFBSActCreateResponseActResultWrapper(
            result=posting_fbs_act_check_status.PostingFBSActCheckStatusResponseResult(
                act_type="act_type",
                added_to_act=["one", "two"],
                removed_from_act=["three", "four"],
                status="status",
            ),
        ),
    ),

    # posting_fbs_act_create.PostingFBSActCreateResponseActResultWrapper
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_act_create.PostingFBSActCreateResponseActResultWrapper(
            result=posting_fbs_act_create.PostingFBSActCreateResponseActResult(
                id=23,
            ),
        ),
    ),

    # posting_fbs_get.GetPostingFBSDataResponseResultWrapper
    _ResponseTestCase(
        kind="second_level_empty",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=None,
                addressee=None,
                analytics_data=None,
                barcodes=None,
                cancellation=None,
                courier=None,
                customer=None,
                delivery_method=None,
                delivery_price="100",
                financial_data=None,
                is_express=False,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=None,
                products=[],
                provider_status="provider status",
                requirements=None,
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
                delivering_date=None,
                in_process_at=None,
                shipment_date=None,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=[],
                addressee=None,
                analytics_data=None,
                barcodes=None,
                cancellation=None,
                courier=None,
                customer=None,
                delivery_method=None,
                delivery_price="100",
                financial_data=None,
                is_express=True,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=None,
                products=[],
                provider_status="provider status",
                requirements=None,
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
                delivering_date=None,
                in_process_at=None,
                shipment_date=None,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=[
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #1",
                        value="value #1",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #2",
                        value="value #2",
                    ),
                ],
                addressee=posting_fbs_get.GetPostingFBSDataResponseAddressee(
                    name="name #1",
                    phone="phone #1",
                ),
                analytics_data=posting_fbs_get.GetPostingFBSDatatResponseAnalyticsData(
                    city="city #1",
                    is_premium=False,
                    payment_type_group_name="payment type group name",
                    region="region #1",
                    tpl_provider="tpl provider #1",
                    tpl_provider_id=1023,
                    warehouse="warehouse #1",
                    warehouse_id=1042,
                    delivery_date_begin=None,
                ),
                barcodes=posting_fbs_get.GetPostingFBSDataResponseBarcodes(
                    lower_barcode="lower barcode",
                    upper_barcode="upper barcode",
                ),
                cancellation=posting_fbs_get.GetPostingFBSDataResponseCancellation(
                    affect_cancellation_rating=False,
                    cancel_reason="cancel reason",
                    cancel_reason_id=2023,
                    cancellation_initiator="cancellation initiator",
                    cancellation_type="cancellation type",
                    cancelled_after_ship=False,
                ),
                courier=posting_fbs_get.GetPostingFBSDataResponseCourier(
                    car_model="car model",
                    car_number="3023",
                    name="name #2",
                    phone="phone #2",
                ),
                customer=posting_fbs_get.GetPostingFBSDataResponseCustomer(
                    address=posting_fbs_get.GetPostingFBSDataResponseAddress(
                        address_tail="address tail",
                        city="city #2",
                        comment="comment",
                        country="country",
                        district="district",
                        latitude=1.01,
                        longitude=1.02,
                        provider_pvz_code="provider pvz code",
                        pvz_code=4023,
                        region="region #2",
                        zip_code="zip code",
                    ),
                    customer_email="customer email",
                    customer_id=5023,
                    name="name #3",
                    phone="phone #3",
                ),
                delivery_method=posting_fbs_get.GetPostingFBSDataResponseDeliveryMethod(
                    id=6023,
                    name="name #4",
                    tpl_provider="tpl provider #2",
                    tpl_provider_id=7023,
                    warehouse="warehouse #2",
                    warehouse_id=8023,
                ),
                delivery_price="100",
                financial_data=posting_fbs_get.GetPostingFBSDataResponseFinancialData(
                    posting_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                        marketplace_service_item_deliv_to_customer=1.03,
                        marketplace_service_item_direct_flow_trans=1.04,
                        marketplace_service_item_dropoff_ff=1.05,
                        marketplace_service_item_dropoff_pvz=1.06,
                        marketplace_service_item_dropoff_sc=1.07,
                        marketplace_service_item_fulfillment=1.08,
                        marketplace_service_item_pickup=1.09,
                        marketplace_service_item_return_after_deliv_to_customer=1.10,
                        marketplace_service_item_return_flow_trans=1.11,
                        marketplace_service_item_return_not_deliv_to_customer=1.12,
                        marketplace_service_item_return_part_goods_customer=1.13,
                    ),
                    products=[],
                ),
                is_express=True,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=posting_fbs_get.GetPostingFBSDataResponseProductExemplars(
                    products=[],
                ),
                products=[
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="9005",
                            length="9012",
                            weight="9023",
                            width="9042",
                        ),
                        mandatory_mark=[],
                        name="name #5",
                        offer_id="10005",
                        price="10012",
                        quantity=10023,
                        sku=10042,
                        currency_code="USD",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="11005",
                            length="11012",
                            weight="11023",
                            width="11042",
                        ),
                        mandatory_mark=[],
                        name="name #6",
                        offer_id="12005",
                        price="12012",
                        quantity=12023,
                        sku=12042,
                        currency_code="EUR",
                    ),
                ],
                provider_status="provider status",
                requirements=posting_fbs_get.GetPostingFBSDataResponseRequirements(
                    products_requiring_gtd=None,
                    products_requiring_country=None,
                    products_requiring_mandatory_mark=None,
                    products_requiring_rnpt=None,
                ),
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
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
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty_list",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=[
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #1",
                        value="value #1",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #2",
                        value="value #2",
                    ),
                ],
                addressee=posting_fbs_get.GetPostingFBSDataResponseAddressee(
                    name="name #1",
                    phone="phone #1",
                ),
                analytics_data=posting_fbs_get.GetPostingFBSDatatResponseAnalyticsData(
                    city="city #1",
                    is_premium=False,
                    payment_type_group_name="payment type group name",
                    region="region #1",
                    tpl_provider="tpl provider #1",
                    tpl_provider_id=1023,
                    warehouse="warehouse #1",
                    warehouse_id=1042,
                    delivery_date_begin=None,
                ),
                barcodes=posting_fbs_get.GetPostingFBSDataResponseBarcodes(
                    lower_barcode="lower barcode",
                    upper_barcode="upper barcode",
                ),
                cancellation=posting_fbs_get.GetPostingFBSDataResponseCancellation(
                    affect_cancellation_rating=False,
                    cancel_reason="cancel reason",
                    cancel_reason_id=2023,
                    cancellation_initiator="cancellation initiator",
                    cancellation_type="cancellation type",
                    cancelled_after_ship=False,
                ),
                courier=posting_fbs_get.GetPostingFBSDataResponseCourier(
                    car_model="car model",
                    car_number="3023",
                    name="name #2",
                    phone="phone #2",
                ),
                customer=posting_fbs_get.GetPostingFBSDataResponseCustomer(
                    address=posting_fbs_get.GetPostingFBSDataResponseAddress(
                        address_tail="address tail",
                        city="city #2",
                        comment="comment",
                        country="country",
                        district="district",
                        latitude=1.01,
                        longitude=1.02,
                        provider_pvz_code="provider pvz code",
                        pvz_code=4023,
                        region="region #2",
                        zip_code="zip code",
                    ),
                    customer_email="customer email",
                    customer_id=5023,
                    name="name #3",
                    phone="phone #3",
                ),
                delivery_method=posting_fbs_get.GetPostingFBSDataResponseDeliveryMethod(
                    id=6023,
                    name="name #4",
                    tpl_provider="tpl provider #2",
                    tpl_provider_id=7023,
                    warehouse="warehouse #2",
                    warehouse_id=8023,
                ),
                delivery_price="100",
                financial_data=posting_fbs_get.GetPostingFBSDataResponseFinancialData(
                    posting_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                        marketplace_service_item_deliv_to_customer=1.03,
                        marketplace_service_item_direct_flow_trans=1.04,
                        marketplace_service_item_dropoff_ff=1.05,
                        marketplace_service_item_dropoff_pvz=1.06,
                        marketplace_service_item_dropoff_sc=1.07,
                        marketplace_service_item_fulfillment=1.08,
                        marketplace_service_item_pickup=1.09,
                        marketplace_service_item_return_after_deliv_to_customer=1.10,
                        marketplace_service_item_return_flow_trans=1.11,
                        marketplace_service_item_return_not_deliv_to_customer=1.12,
                        marketplace_service_item_return_part_goods_customer=1.13,
                    ),
                    products=[],
                ),
                is_express=True,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=posting_fbs_get.GetPostingFBSDataResponseProductExemplars(
                    products=[],
                ),
                products=[
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="9005",
                            length="9012",
                            weight="9023",
                            width="9042",
                        ),
                        mandatory_mark=[],
                        name="name #5",
                        offer_id="10005",
                        price="10012",
                        quantity=10023,
                        sku=10042,
                        currency_code="USD",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="11005",
                            length="11012",
                            weight="11023",
                            width="11042",
                        ),
                        mandatory_mark=[],
                        name="name #6",
                        offer_id="12005",
                        price="12012",
                        quantity=12023,
                        sku=12042,
                        currency_code="EUR",
                    ),
                ],
                provider_status="provider status",
                requirements=posting_fbs_get.GetPostingFBSDataResponseRequirements(
                    products_requiring_gtd=[],
                    products_requiring_country=[],
                    products_requiring_mandatory_mark=[],
                    products_requiring_rnpt=[],
                ),
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
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
        ),
    ),
    _ResponseTestCase(
        kind="fourth_level_empty_list",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=[
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #1",
                        value="value #1",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #2",
                        value="value #2",
                    ),
                ],
                addressee=posting_fbs_get.GetPostingFBSDataResponseAddressee(
                    name="name #1",
                    phone="phone #1",
                ),
                analytics_data=posting_fbs_get.GetPostingFBSDatatResponseAnalyticsData(
                    city="city #1",
                    is_premium=True,
                    payment_type_group_name="payment type group name",
                    region="region #1",
                    tpl_provider="tpl provider #1",
                    tpl_provider_id=1023,
                    warehouse="warehouse #1",
                    warehouse_id=1042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-02T21:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_get.GetPostingFBSDataResponseBarcodes(
                    lower_barcode="lower barcode",
                    upper_barcode="upper barcode",
                ),
                cancellation=posting_fbs_get.GetPostingFBSDataResponseCancellation(
                    affect_cancellation_rating=True,
                    cancel_reason="cancel reason",
                    cancel_reason_id=2023,
                    cancellation_initiator="cancellation initiator",
                    cancellation_type="cancellation type",
                    cancelled_after_ship=True,
                ),
                courier=posting_fbs_get.GetPostingFBSDataResponseCourier(
                    car_model="car model",
                    car_number="3023",
                    name="name #2",
                    phone="phone #2",
                ),
                customer=posting_fbs_get.GetPostingFBSDataResponseCustomer(
                    address=posting_fbs_get.GetPostingFBSDataResponseAddress(
                        address_tail="address tail",
                        city="city #2",
                        comment="comment",
                        country="country",
                        district="district",
                        latitude=1.01,
                        longitude=1.02,
                        provider_pvz_code="provider pvz code",
                        pvz_code=4023,
                        region="region #2",
                        zip_code="zip code",
                    ),
                    customer_email="customer email",
                    customer_id=5023,
                    name="name #3",
                    phone="phone #3",
                ),
                delivery_method=posting_fbs_get.GetPostingFBSDataResponseDeliveryMethod(
                    id=6023,
                    name="name #4",
                    tpl_provider="tpl provider #2",
                    tpl_provider_id=7023,
                    warehouse="warehouse #2",
                    warehouse_id=8023,
                ),
                delivery_price="100",
                financial_data=posting_fbs_get.GetPostingFBSDataResponseFinancialData(
                    posting_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                        marketplace_service_item_deliv_to_customer=1.03,
                        marketplace_service_item_direct_flow_trans=1.04,
                        marketplace_service_item_dropoff_ff=1.05,
                        marketplace_service_item_dropoff_pvz=1.06,
                        marketplace_service_item_dropoff_sc=1.07,
                        marketplace_service_item_fulfillment=1.08,
                        marketplace_service_item_pickup=1.09,
                        marketplace_service_item_return_after_deliv_to_customer=1.10,
                        marketplace_service_item_return_flow_trans=1.11,
                        marketplace_service_item_return_not_deliv_to_customer=1.12,
                        marketplace_service_item_return_part_goods_customer=1.13,
                    ),
                    products=[
                        posting_fbs_get.GetPostingFBSDataResponseDataProduct(
                            actions=[],
                            client_price="100005",
                            commission_amount=1.14,
                            commission_percent=23,
                            item_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=10.01,
                                marketplace_service_item_direct_flow_trans=10.02,
                                marketplace_service_item_dropoff_ff=10.03,
                                marketplace_service_item_dropoff_pvz=10.04,
                                marketplace_service_item_dropoff_sc=10.05,
                                marketplace_service_item_fulfillment=10.06,
                                marketplace_service_item_pickup=10.07,
                                marketplace_service_item_return_after_deliv_to_customer=10.08,
                                marketplace_service_item_return_flow_trans=10.09,
                                marketplace_service_item_return_not_deliv_to_customer=10.10,
                                marketplace_service_item_return_part_goods_customer=10.11,
                            ),
                            old_price=1.15,
                            payout=1.16,
                            picking=posting_fbs_get.GetPostingFBSDataResponseFinancialPicking(
                                amount=10.12,
                                tag="tag #1",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T23:04:05.999999+07:00",
                                ),
                            ),
                            price=1.17,
                            product_id=100012,
                            quantity=100023,
                            total_discount_percent=1.18,
                            total_discount_value=1.19,
                        ),
                        posting_fbs_get.GetPostingFBSDataResponseDataProduct(
                            actions=[],
                            client_price="200005",
                            commission_amount=1.20,
                            commission_percent=42,
                            item_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=20.01,
                                marketplace_service_item_direct_flow_trans=20.02,
                                marketplace_service_item_dropoff_ff=20.03,
                                marketplace_service_item_dropoff_pvz=20.04,
                                marketplace_service_item_dropoff_sc=20.05,
                                marketplace_service_item_fulfillment=20.06,
                                marketplace_service_item_pickup=20.07,
                                marketplace_service_item_return_after_deliv_to_customer=20.08,
                                marketplace_service_item_return_flow_trans=20.09,
                                marketplace_service_item_return_not_deliv_to_customer=20.10,
                                marketplace_service_item_return_part_goods_customer=20.11,
                            ),
                            old_price=1.21,
                            payout=1.22,
                            picking=posting_fbs_get.GetPostingFBSDataResponseFinancialPicking(
                                amount=20.12,
                                tag="tag #2",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T01:04:05.999999+07:00",
                                ),
                            ),
                            price=1.23,
                            product_id=200012,
                            quantity=200023,
                            total_discount_percent=1.24,
                            total_discount_value=1.25,
                        ),
                    ],
                ),
                is_express=True,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=posting_fbs_get.GetPostingFBSDataResponseProductExemplars(
                    products=[
                        posting_fbs_get.GetPostingFBSDataResponseExemplarProduct(
                            exemplars=[],
                            sku=1000023,
                        ),
                        posting_fbs_get.GetPostingFBSDataResponseExemplarProduct(
                            exemplars=[],
                            sku=2000023,
                        ),
                    ],
                ),
                products=[
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="9005",
                            length="9012",
                            weight="9023",
                            width="9042",
                        ),
                        mandatory_mark=["mandatory mark #1", "mandatory mark #2"],
                        name="name #5",
                        offer_id="10005",
                        price="10012",
                        quantity=10023,
                        sku=10042,
                        currency_code="USD",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="11005",
                            length="11012",
                            weight="11023",
                            width="11042",
                        ),
                        mandatory_mark=["mandatory mark #3", "mandatory mark #4"],
                        name="name #6",
                        offer_id="12005",
                        price="12012",
                        quantity=12023,
                        sku=12042,
                        currency_code="EUR",
                    ),
                ],
                provider_status="provider status",
                requirements=posting_fbs_get.GetPostingFBSDataResponseRequirements(
                    products_requiring_gtd=[10000001, 10000002],
                    products_requiring_country=[10000003, 10000004],
                    products_requiring_mandatory_mark=[10000005, 10000006],
                    products_requiring_rnpt=[10000007, 10000008],
                ),
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
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
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_get.GetPostingFBSDataResponseResultWrapper(
            result=posting_fbs_get.GetPostingFBSDataResponseResult(
                additional_data=[
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #1",
                        value="value #1",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseAdditionalDataItem(
                        key="key #2",
                        value="value #2",
                    ),
                ],
                addressee=posting_fbs_get.GetPostingFBSDataResponseAddressee(
                    name="name #1",
                    phone="phone #1",
                ),
                analytics_data=posting_fbs_get.GetPostingFBSDatatResponseAnalyticsData(
                    city="city #1",
                    is_premium=True,
                    payment_type_group_name="payment type group name",
                    region="region #1",
                    tpl_provider="tpl provider #1",
                    tpl_provider_id=1023,
                    warehouse="warehouse #1",
                    warehouse_id=1042,
                    delivery_date_begin=datetime.datetime.fromisoformat(
                        "2006-01-02T21:04:05.999999+07:00",
                    ),
                ),
                barcodes=posting_fbs_get.GetPostingFBSDataResponseBarcodes(
                    lower_barcode="lower barcode",
                    upper_barcode="upper barcode",
                ),
                cancellation=posting_fbs_get.GetPostingFBSDataResponseCancellation(
                    affect_cancellation_rating=True,
                    cancel_reason="cancel reason",
                    cancel_reason_id=2023,
                    cancellation_initiator="cancellation initiator",
                    cancellation_type="cancellation type",
                    cancelled_after_ship=True,
                ),
                courier=posting_fbs_get.GetPostingFBSDataResponseCourier(
                    car_model="car model",
                    car_number="3023",
                    name="name #2",
                    phone="phone #2",
                ),
                customer=posting_fbs_get.GetPostingFBSDataResponseCustomer(
                    address=posting_fbs_get.GetPostingFBSDataResponseAddress(
                        address_tail="address tail",
                        city="city #2",
                        comment="comment",
                        country="country",
                        district="district",
                        latitude=1.01,
                        longitude=1.02,
                        provider_pvz_code="provider pvz code",
                        pvz_code=4023,
                        region="region #2",
                        zip_code="zip code",
                    ),
                    customer_email="customer email",
                    customer_id=5023,
                    name="name #3",
                    phone="phone #3",
                ),
                delivery_method=posting_fbs_get.GetPostingFBSDataResponseDeliveryMethod(
                    id=6023,
                    name="name #4",
                    tpl_provider="tpl provider #2",
                    tpl_provider_id=7023,
                    warehouse="warehouse #2",
                    warehouse_id=8023,
                ),
                delivery_price="100",
                financial_data=posting_fbs_get.GetPostingFBSDataResponseFinancialData(
                    posting_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                        marketplace_service_item_deliv_to_customer=1.03,
                        marketplace_service_item_direct_flow_trans=1.04,
                        marketplace_service_item_dropoff_ff=1.05,
                        marketplace_service_item_dropoff_pvz=1.06,
                        marketplace_service_item_dropoff_sc=1.07,
                        marketplace_service_item_fulfillment=1.08,
                        marketplace_service_item_pickup=1.09,
                        marketplace_service_item_return_after_deliv_to_customer=1.10,
                        marketplace_service_item_return_flow_trans=1.11,
                        marketplace_service_item_return_not_deliv_to_customer=1.12,
                        marketplace_service_item_return_part_goods_customer=1.13,
                    ),
                    products=[
                        posting_fbs_get.GetPostingFBSDataResponseDataProduct(
                            actions=["action #1", "action #2"],
                            client_price="100005",
                            commission_amount=1.14,
                            commission_percent=23,
                            item_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=10.01,
                                marketplace_service_item_direct_flow_trans=10.02,
                                marketplace_service_item_dropoff_ff=10.03,
                                marketplace_service_item_dropoff_pvz=10.04,
                                marketplace_service_item_dropoff_sc=10.05,
                                marketplace_service_item_fulfillment=10.06,
                                marketplace_service_item_pickup=10.07,
                                marketplace_service_item_return_after_deliv_to_customer=10.08,
                                marketplace_service_item_return_flow_trans=10.09,
                                marketplace_service_item_return_not_deliv_to_customer=10.10,
                                marketplace_service_item_return_part_goods_customer=10.11,
                            ),
                            old_price=1.15,
                            payout=1.16,
                            picking=posting_fbs_get.GetPostingFBSDataResponseFinancialPicking(
                                amount=10.12,
                                tag="tag #1",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-02T23:04:05.999999+07:00",
                                ),
                            ),
                            price=1.17,
                            product_id=100012,
                            quantity=100023,
                            total_discount_percent=1.18,
                            total_discount_value=1.19,
                        ),
                        posting_fbs_get.GetPostingFBSDataResponseDataProduct(
                            actions=["action #3", "action #4"],
                            client_price="200005",
                            commission_amount=1.20,
                            commission_percent=42,
                            item_services=posting_fbs_get.GetPostingFBSDataResponseFinancialDataServices(
                                marketplace_service_item_deliv_to_customer=20.01,
                                marketplace_service_item_direct_flow_trans=20.02,
                                marketplace_service_item_dropoff_ff=20.03,
                                marketplace_service_item_dropoff_pvz=20.04,
                                marketplace_service_item_dropoff_sc=20.05,
                                marketplace_service_item_fulfillment=20.06,
                                marketplace_service_item_pickup=20.07,
                                marketplace_service_item_return_after_deliv_to_customer=20.08,
                                marketplace_service_item_return_flow_trans=20.09,
                                marketplace_service_item_return_not_deliv_to_customer=20.10,
                                marketplace_service_item_return_part_goods_customer=20.11,
                            ),
                            old_price=1.21,
                            payout=1.22,
                            picking=posting_fbs_get.GetPostingFBSDataResponseFinancialPicking(
                                amount=20.12,
                                tag="tag #2",
                                moment=datetime.datetime.fromisoformat(
                                    "2006-01-03T01:04:05.999999+07:00",
                                ),
                            ),
                            price=1.23,
                            product_id=200012,
                            quantity=200023,
                            total_discount_percent=1.24,
                            total_discount_value=1.25,
                        ),
                    ],
                ),
                is_express=True,
                order_id=105,
                order_number="112",
                posting_number="123",
                product_exemplars=posting_fbs_get.GetPostingFBSDataResponseProductExemplars(
                    products=[
                        posting_fbs_get.GetPostingFBSDataResponseExemplarProduct(
                            exemplars=[
                                posting_fbs_get.GetPostingFBSDataResponseExemplarProductInfo(
                                    mandatory_mark="mandatory mark #1",
                                    gtd="gtd #1",
                                    is_gtd_absent=False,
                                    rnpt="rnpt #1",
                                    is_rnpt_absent=False,
                                ),
                                posting_fbs_get.GetPostingFBSDataResponseExemplarProductInfo(
                                    mandatory_mark="mandatory mark #2",
                                    gtd="gtd #2",
                                    is_gtd_absent=True,
                                    rnpt="rnpt #2",
                                    is_rnpt_absent=True,
                                ),
                            ],
                            sku=1000023,
                        ),
                        posting_fbs_get.GetPostingFBSDataResponseExemplarProduct(
                            exemplars=[
                                posting_fbs_get.GetPostingFBSDataResponseExemplarProductInfo(
                                    mandatory_mark="mandatory mark #3",
                                    gtd="gtd #3",
                                    is_gtd_absent=False,
                                    rnpt="rnpt #3",
                                    is_rnpt_absent=False,
                                ),
                                posting_fbs_get.GetPostingFBSDataResponseExemplarProductInfo(
                                    mandatory_mark="mandatory mark #4",
                                    gtd="gtd #4",
                                    is_gtd_absent=True,
                                    rnpt="rnpt #4",
                                    is_rnpt_absent=True,
                                ),
                            ],
                            sku=2000023,
                        ),
                    ],
                ),
                products=[
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="9005",
                            length="9012",
                            weight="9023",
                            width="9042",
                        ),
                        mandatory_mark=["mandatory mark #1", "mandatory mark #2"],
                        name="name #5",
                        offer_id="10005",
                        price="10012",
                        quantity=10023,
                        sku=10042,
                        currency_code="USD",
                    ),
                    posting_fbs_get.GetPostingFBSDataResponseProduct(
                        dimensions=posting_fbs_get.GetPostingFBSDataResponseDimensions(
                            height="11005",
                            length="11012",
                            weight="11023",
                            width="11042",
                        ),
                        mandatory_mark=["mandatory mark #3", "mandatory mark #4"],
                        name="name #6",
                        offer_id="12005",
                        price="12012",
                        quantity=12023,
                        sku=12042,
                        currency_code="EUR",
                    ),
                ],
                provider_status="provider status",
                requirements=posting_fbs_get.GetPostingFBSDataResponseRequirements(
                    products_requiring_gtd=[10000001, 10000002],
                    products_requiring_country=[10000003, 10000004],
                    products_requiring_mandatory_mark=[10000005, 10000006],
                    products_requiring_rnpt=[10000007, 10000008],
                ),
                status="status",
                tpl_integration_type="tpl integration type",
                tracking_number="142",
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
        ),
    ),

    # posting_fbs_list.GetPostingFBSListResponseResultWrapper
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=posting_fbs_list.GetPostingFBSListResponseResultWrapper(
            result=posting_fbs_list.GetPostingFBSListResponseResult(
                postings=[],
                has_next=False,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty_list",
        expected_data=posting_fbs_list.GetPostingFBSListResponseResultWrapper(
            result=posting_fbs_list.GetPostingFBSListResponseResult(
                postings=[
                    posting_fbs_list.GetPostingFBSListResponsePosting(
                        addressee=None,
                        analytics_data=None,
                        barcodes=None,
                        cancellation=None,
                        customer=None,
                        delivery_method=None,
                        financial_data=None,
                        is_express=False,
                        order_id=105,
                        order_number="112",
                        posting_number="123",
                        products=[],
                        requirements=None,
                        status="status #1",
                        tpl_integration_type="tpl integration type #1",
                        tracking_number="142",
                        delivering_date=None,
                        in_process_at=None,
                        shipment_date=None,
                    ),
                    posting_fbs_list.GetPostingFBSListResponsePosting(
                        addressee=None,
                        analytics_data=None,
                        barcodes=None,
                        cancellation=None,
                        customer=None,
                        delivery_method=None,
                        financial_data=None,
                        is_express=True,
                        order_id=205,
                        order_number="212",
                        posting_number="223",
                        products=[],
                        requirements=None,
                        status="status #2",
                        tpl_integration_type="tpl integration type #2",
                        tracking_number="242",
                        delivering_date=None,
                        in_process_at=None,
                        shipment_date=None,
                    ),
                ],
                has_next=True,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="fourth_level_empty_list",
        expected_data=posting_fbs_list.GetPostingFBSListResponseResultWrapper(
            result=posting_fbs_list.GetPostingFBSListResponseResult(
                postings=[
                    posting_fbs_list.GetPostingFBSListResponsePosting(
                        addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                            name="name #11",
                            phone="phone #11",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #11",
                            is_premium=False,
                            payment_type_group_name="payment type group name #11",
                            region="region #11",
                            tpl_provider="tpl provider #11",
                            tpl_provider_id=11023,
                            warehouse="warehouse #11",
                            warehouse_id=11042,
                            delivery_date_begin=None,
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #11",
                            upper_barcode="upper barcode #11",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=False,
                            cancel_reason="cancel reason #11",
                            cancel_reason_id=12023,
                            cancellation_initiator="cancellation initiator #11",
                            cancellation_type="cancellation type #11",
                            cancelled_after_ship=False,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #11",
                                city="city #12",
                                comment="comment #11",
                                country="country #11",
                                district="district #11",
                                latitude=11.01,
                                longitude=11.02,
                                provider_pvz_code="provider pvz code #11",
                                pvz_code=13042,
                                region="region #11",
                                zip_code="zip code #11",
                            ),
                            customer_email="customer email #11",
                            customer_id=13023,
                            name="name #12",
                            phone="phone #12",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=14012,
                            name="name #13",
                            tpl_provider="tpl provider #12",
                            tpl_provider_id=14023,
                            warehouse="warehouse #12",
                            warehouse_id=14042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=11.03,
                                    marketplace_service_item_direct_flow_trans=11.04,
                                    marketplace_service_item_dropoff_ff=11.05,
                                    marketplace_service_item_dropoff_pvz=11.06,
                                    marketplace_service_item_dropoff_sc=11.07,
                                    marketplace_service_item_fulfillment=11.08,
                                    marketplace_service_item_pickup=11.09,
                                    marketplace_service_item_return_after_deliv_to_customer=11.10,
                                    marketplace_service_item_return_flow_trans=11.11,
                                    marketplace_service_item_return_not_deliv_to_customer=11.12,
                                    marketplace_service_item_return_part_goods_customer=11.13,
                                ),
                            products=[],
                        ),
                        is_express=False,
                        order_id=105,
                        order_number="112",
                        posting_number="123",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=[],
                                name="name #14",
                                offer_id="15005",
                                price="15012",
                                quantity=15023,
                                sku=15042,
                                currency_code="currency code #11",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=[],
                                name="name #15",
                                offer_id="16005",
                                price="16012",
                                quantity=16023,
                                sku=16042,
                                currency_code="currency code #12",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=None,
                            products_requiring_country=None,
                            products_requiring_mandatory_mark=None,
                            products_requiring_rnpt=None,
                        ),
                        status="status #1",
                        tpl_integration_type="tpl integration type #1",
                        tracking_number="142",
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
                            name="name #21",
                            phone="phone #21",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #21",
                            is_premium=True,
                            payment_type_group_name="payment type group name #21",
                            region="region #21",
                            tpl_provider="tpl provider #21",
                            tpl_provider_id=21023,
                            warehouse="warehouse #21",
                            warehouse_id=21042,
                            delivery_date_begin=None,
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #21",
                            upper_barcode="upper barcode #21",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=True,
                            cancel_reason="cancel reason #21",
                            cancel_reason_id=22023,
                            cancellation_initiator="cancellation initiator #21",
                            cancellation_type="cancellation type #21",
                            cancelled_after_ship=True,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #21",
                                city="city #22",
                                comment="comment #21",
                                country="country #21",
                                district="district #21",
                                latitude=21.01,
                                longitude=21.02,
                                provider_pvz_code="provider pvz code #21",
                                pvz_code=23042,
                                region="region #21",
                                zip_code="zip code #21",
                            ),
                            customer_email="customer email #21",
                            customer_id=23023,
                            name="name #22",
                            phone="phone #22",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=24012,
                            name="name #23",
                            tpl_provider="tpl provider #22",
                            tpl_provider_id=24023,
                            warehouse="warehouse #22",
                            warehouse_id=24042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=21.03,
                                    marketplace_service_item_direct_flow_trans=21.04,
                                    marketplace_service_item_dropoff_ff=21.05,
                                    marketplace_service_item_dropoff_pvz=21.06,
                                    marketplace_service_item_dropoff_sc=21.07,
                                    marketplace_service_item_fulfillment=21.08,
                                    marketplace_service_item_pickup=21.09,
                                    marketplace_service_item_return_after_deliv_to_customer=21.10,
                                    marketplace_service_item_return_flow_trans=21.11,
                                    marketplace_service_item_return_not_deliv_to_customer=21.12,
                                    marketplace_service_item_return_part_goods_customer=21.13,
                                ),
                            products=[],
                        ),
                        is_express=True,
                        order_id=205,
                        order_number="212",
                        posting_number="223",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=[],
                                name="name #24",
                                offer_id="25005",
                                price="25012",
                                quantity=25023,
                                sku=25042,
                                currency_code="currency code #21",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=[],
                                name="name #25",
                                offer_id="26005",
                                price="26012",
                                quantity=26023,
                                sku=26042,
                                currency_code="currency code #22",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=None,
                            products_requiring_country=None,
                            products_requiring_mandatory_mark=None,
                            products_requiring_rnpt=None,
                        ),
                        status="status #2",
                        tpl_integration_type="tpl integration type #2",
                        tracking_number="242",
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
                has_next=True,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="fifth_level_empty_list",
        expected_data=posting_fbs_list.GetPostingFBSListResponseResultWrapper(
            result=posting_fbs_list.GetPostingFBSListResponseResult(
                postings=[
                    posting_fbs_list.GetPostingFBSListResponsePosting(
                        addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                            name="name #11",
                            phone="phone #11",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #11",
                            is_premium=False,
                            payment_type_group_name="payment type group name #11",
                            region="region #11",
                            tpl_provider="tpl provider #11",
                            tpl_provider_id=11023,
                            warehouse="warehouse #11",
                            warehouse_id=11042,
                            delivery_date_begin=datetime.datetime.fromisoformat(
                                "2006-01-03T01:04:05.999999+07:00",
                            ),
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #11",
                            upper_barcode="upper barcode #11",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=False,
                            cancel_reason="cancel reason #11",
                            cancel_reason_id=12023,
                            cancellation_initiator="cancellation initiator #11",
                            cancellation_type="cancellation type #11",
                            cancelled_after_ship=False,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #11",
                                city="city #12",
                                comment="comment #11",
                                country="country #11",
                                district="district #11",
                                latitude=11.01,
                                longitude=11.02,
                                provider_pvz_code="provider pvz code #11",
                                pvz_code=13042,
                                region="region #11",
                                zip_code="zip code #11",
                            ),
                            customer_email="customer email #11",
                            customer_id=13023,
                            name="name #12",
                            phone="phone #12",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=14012,
                            name="name #13",
                            tpl_provider="tpl provider #12",
                            tpl_provider_id=14023,
                            warehouse="warehouse #12",
                            warehouse_id=14042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=11.03,
                                    marketplace_service_item_direct_flow_trans=11.04,
                                    marketplace_service_item_dropoff_ff=11.05,
                                    marketplace_service_item_dropoff_pvz=11.06,
                                    marketplace_service_item_dropoff_sc=11.07,
                                    marketplace_service_item_fulfillment=11.08,
                                    marketplace_service_item_pickup=11.09,
                                    marketplace_service_item_return_after_deliv_to_customer=11.10,
                                    marketplace_service_item_return_flow_trans=11.11,
                                    marketplace_service_item_return_not_deliv_to_customer=11.12,
                                    marketplace_service_item_return_part_goods_customer=11.13,
                                ),
                            products=[
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=[],
                                    client_price="17005",
                                    commission_amount=11.14,
                                    commission_percent=17012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=11.20,
                                            marketplace_service_item_direct_flow_trans=11.21,
                                            marketplace_service_item_dropoff_ff=11.22,
                                            marketplace_service_item_dropoff_pvz=11.23,
                                            marketplace_service_item_dropoff_sc=11.24,
                                            marketplace_service_item_fulfillment=11.25,
                                            marketplace_service_item_pickup=11.26,
                                            marketplace_service_item_return_after_deliv_to_customer=11.27,
                                            marketplace_service_item_return_flow_trans=11.28,
                                            marketplace_service_item_return_not_deliv_to_customer=11.29,
                                            marketplace_service_item_return_part_goods_customer=11.30,
                                        ),
                                    old_price=11.15,
                                    payout=11.16,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=11.31,
                                        tag="tag #11",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-02T21:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=11.17,
                                    product_id=17023,
                                    quantity=17042,
                                    total_discount_percent=11.18,
                                    total_discount_value=11.19,
                                ),
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=[],
                                    client_price="18005",
                                    commission_amount=11.32,
                                    commission_percent=18012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=11.38,
                                            marketplace_service_item_direct_flow_trans=11.39,
                                            marketplace_service_item_dropoff_ff=11.40,
                                            marketplace_service_item_dropoff_pvz=11.41,
                                            marketplace_service_item_dropoff_sc=11.42,
                                            marketplace_service_item_fulfillment=11.43,
                                            marketplace_service_item_pickup=11.44,
                                            marketplace_service_item_return_after_deliv_to_customer=11.45,
                                            marketplace_service_item_return_flow_trans=11.46,
                                            marketplace_service_item_return_not_deliv_to_customer=11.47,
                                            marketplace_service_item_return_part_goods_customer=11.48,
                                        ),
                                    old_price=11.33,
                                    payout=11.34,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=11.49,
                                        tag="tag #12",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-02T23:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=11.35,
                                    product_id=18023,
                                    quantity=18042,
                                    total_discount_percent=11.36,
                                    total_discount_value=11.37,
                                ),
                            ],
                        ),
                        is_express=False,
                        order_id=105,
                        order_number="112",
                        posting_number="123",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #1", "mandatory mark #2"],
                                name="name #14",
                                offer_id="15005",
                                price="15012",
                                quantity=15023,
                                sku=15042,
                                currency_code="currency code #11",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #3", "mandatory mark #4"],
                                name="name #15",
                                offer_id="16005",
                                price="16012",
                                quantity=16023,
                                sku=16042,
                                currency_code="currency code #12",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=[],
                            products_requiring_country=[],
                            products_requiring_mandatory_mark=[],
                            products_requiring_rnpt=[],
                        ),
                        status="status #1",
                        tpl_integration_type="tpl integration type #1",
                        tracking_number="142",
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
                            name="name #21",
                            phone="phone #21",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #21",
                            is_premium=True,
                            payment_type_group_name="payment type group name #21",
                            region="region #21",
                            tpl_provider="tpl provider #21",
                            tpl_provider_id=21023,
                            warehouse="warehouse #21",
                            warehouse_id=21042,
                            delivery_date_begin=datetime.datetime.fromisoformat(
                                "2006-01-04T01:04:05.999999+07:00",
                            ),
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #21",
                            upper_barcode="upper barcode #21",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=True,
                            cancel_reason="cancel reason #21",
                            cancel_reason_id=22023,
                            cancellation_initiator="cancellation initiator #21",
                            cancellation_type="cancellation type #21",
                            cancelled_after_ship=True,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #21",
                                city="city #22",
                                comment="comment #21",
                                country="country #21",
                                district="district #21",
                                latitude=21.01,
                                longitude=21.02,
                                provider_pvz_code="provider pvz code #21",
                                pvz_code=23042,
                                region="region #21",
                                zip_code="zip code #21",
                            ),
                            customer_email="customer email #21",
                            customer_id=23023,
                            name="name #22",
                            phone="phone #22",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=24012,
                            name="name #23",
                            tpl_provider="tpl provider #22",
                            tpl_provider_id=24023,
                            warehouse="warehouse #22",
                            warehouse_id=24042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=21.03,
                                    marketplace_service_item_direct_flow_trans=21.04,
                                    marketplace_service_item_dropoff_ff=21.05,
                                    marketplace_service_item_dropoff_pvz=21.06,
                                    marketplace_service_item_dropoff_sc=21.07,
                                    marketplace_service_item_fulfillment=21.08,
                                    marketplace_service_item_pickup=21.09,
                                    marketplace_service_item_return_after_deliv_to_customer=21.10,
                                    marketplace_service_item_return_flow_trans=21.11,
                                    marketplace_service_item_return_not_deliv_to_customer=21.12,
                                    marketplace_service_item_return_part_goods_customer=21.13,
                                ),
                            products=[
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=[],
                                    client_price="27005",
                                    commission_amount=21.14,
                                    commission_percent=27012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=21.20,
                                            marketplace_service_item_direct_flow_trans=21.21,
                                            marketplace_service_item_dropoff_ff=21.22,
                                            marketplace_service_item_dropoff_pvz=21.23,
                                            marketplace_service_item_dropoff_sc=21.24,
                                            marketplace_service_item_fulfillment=21.25,
                                            marketplace_service_item_pickup=21.26,
                                            marketplace_service_item_return_after_deliv_to_customer=21.27,
                                            marketplace_service_item_return_flow_trans=21.28,
                                            marketplace_service_item_return_not_deliv_to_customer=21.29,
                                            marketplace_service_item_return_part_goods_customer=21.30,
                                        ),
                                    old_price=21.15,
                                    payout=21.16,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=21.31,
                                        tag="tag #21",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-03T21:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=21.17,
                                    product_id=27023,
                                    quantity=27042,
                                    total_discount_percent=21.18,
                                    total_discount_value=21.19,
                                ),
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=[],
                                    client_price="28005",
                                    commission_amount=21.32,
                                    commission_percent=28012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=21.38,
                                            marketplace_service_item_direct_flow_trans=21.39,
                                            marketplace_service_item_dropoff_ff=21.40,
                                            marketplace_service_item_dropoff_pvz=21.41,
                                            marketplace_service_item_dropoff_sc=21.42,
                                            marketplace_service_item_fulfillment=21.43,
                                            marketplace_service_item_pickup=21.44,
                                            marketplace_service_item_return_after_deliv_to_customer=21.45,
                                            marketplace_service_item_return_flow_trans=21.46,
                                            marketplace_service_item_return_not_deliv_to_customer=21.47,
                                            marketplace_service_item_return_part_goods_customer=21.48,
                                        ),
                                    old_price=21.33,
                                    payout=21.34,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=21.49,
                                        tag="tag #22",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-03T23:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=21.35,
                                    product_id=28023,
                                    quantity=28042,
                                    total_discount_percent=21.36,
                                    total_discount_value=21.37,
                                ),
                            ],
                        ),
                        is_express=True,
                        order_id=205,
                        order_number="212",
                        posting_number="223",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #5", "mandatory mark #6"],
                                name="name #24",
                                offer_id="25005",
                                price="25012",
                                quantity=25023,
                                sku=25042,
                                currency_code="currency code #21",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #7", "mandatory mark #8"],
                                name="name #25",
                                offer_id="26005",
                                price="26012",
                                quantity=26023,
                                sku=26042,
                                currency_code="currency code #22",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=[],
                            products_requiring_country=[],
                            products_requiring_mandatory_mark=[],
                            products_requiring_rnpt=[],
                        ),
                        status="status #2",
                        tpl_integration_type="tpl integration type #2",
                        tracking_number="242",
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
                has_next=True,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_list.GetPostingFBSListResponseResultWrapper(
            result=posting_fbs_list.GetPostingFBSListResponseResult(
                postings=[
                    posting_fbs_list.GetPostingFBSListResponsePosting(
                        addressee=posting_fbs_list.GetPostingFBSListResponseAddressee(
                            name="name #11",
                            phone="phone #11",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #11",
                            is_premium=False,
                            payment_type_group_name="payment type group name #11",
                            region="region #11",
                            tpl_provider="tpl provider #11",
                            tpl_provider_id=11023,
                            warehouse="warehouse #11",
                            warehouse_id=11042,
                            delivery_date_begin=datetime.datetime.fromisoformat(
                                "2006-01-03T01:04:05.999999+07:00",
                            ),
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #11",
                            upper_barcode="upper barcode #11",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=False,
                            cancel_reason="cancel reason #11",
                            cancel_reason_id=12023,
                            cancellation_initiator="cancellation initiator #11",
                            cancellation_type="cancellation type #11",
                            cancelled_after_ship=False,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #11",
                                city="city #12",
                                comment="comment #11",
                                country="country #11",
                                district="district #11",
                                latitude=11.01,
                                longitude=11.02,
                                provider_pvz_code="provider pvz code #11",
                                pvz_code=13042,
                                region="region #11",
                                zip_code="zip code #11",
                            ),
                            customer_email="customer email #11",
                            customer_id=13023,
                            name="name #12",
                            phone="phone #12",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=14012,
                            name="name #13",
                            tpl_provider="tpl provider #12",
                            tpl_provider_id=14023,
                            warehouse="warehouse #12",
                            warehouse_id=14042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=11.03,
                                    marketplace_service_item_direct_flow_trans=11.04,
                                    marketplace_service_item_dropoff_ff=11.05,
                                    marketplace_service_item_dropoff_pvz=11.06,
                                    marketplace_service_item_dropoff_sc=11.07,
                                    marketplace_service_item_fulfillment=11.08,
                                    marketplace_service_item_pickup=11.09,
                                    marketplace_service_item_return_after_deliv_to_customer=11.10,
                                    marketplace_service_item_return_flow_trans=11.11,
                                    marketplace_service_item_return_not_deliv_to_customer=11.12,
                                    marketplace_service_item_return_part_goods_customer=11.13,
                                ),
                            products=[
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=["action #1", "action #2"],
                                    client_price="17005",
                                    commission_amount=11.14,
                                    commission_percent=17012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=11.20,
                                            marketplace_service_item_direct_flow_trans=11.21,
                                            marketplace_service_item_dropoff_ff=11.22,
                                            marketplace_service_item_dropoff_pvz=11.23,
                                            marketplace_service_item_dropoff_sc=11.24,
                                            marketplace_service_item_fulfillment=11.25,
                                            marketplace_service_item_pickup=11.26,
                                            marketplace_service_item_return_after_deliv_to_customer=11.27,
                                            marketplace_service_item_return_flow_trans=11.28,
                                            marketplace_service_item_return_not_deliv_to_customer=11.29,
                                            marketplace_service_item_return_part_goods_customer=11.30,
                                        ),
                                    old_price=11.15,
                                    payout=11.16,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=11.31,
                                        tag="tag #11",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-02T21:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=11.17,
                                    product_id=17023,
                                    quantity=17042,
                                    total_discount_percent=11.18,
                                    total_discount_value=11.19,
                                ),
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=["action #3", "action #4"],
                                    client_price="18005",
                                    commission_amount=11.32,
                                    commission_percent=18012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=11.38,
                                            marketplace_service_item_direct_flow_trans=11.39,
                                            marketplace_service_item_dropoff_ff=11.40,
                                            marketplace_service_item_dropoff_pvz=11.41,
                                            marketplace_service_item_dropoff_sc=11.42,
                                            marketplace_service_item_fulfillment=11.43,
                                            marketplace_service_item_pickup=11.44,
                                            marketplace_service_item_return_after_deliv_to_customer=11.45,
                                            marketplace_service_item_return_flow_trans=11.46,
                                            marketplace_service_item_return_not_deliv_to_customer=11.47,
                                            marketplace_service_item_return_part_goods_customer=11.48,
                                        ),
                                    old_price=11.33,
                                    payout=11.34,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=11.49,
                                        tag="tag #12",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-02T23:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=11.35,
                                    product_id=18023,
                                    quantity=18042,
                                    total_discount_percent=11.36,
                                    total_discount_value=11.37,
                                ),
                            ],
                        ),
                        is_express=False,
                        order_id=105,
                        order_number="112",
                        posting_number="123",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #1", "mandatory mark #2"],
                                name="name #14",
                                offer_id="15005",
                                price="15012",
                                quantity=15023,
                                sku=15042,
                                currency_code="currency code #11",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #3", "mandatory mark #4"],
                                name="name #15",
                                offer_id="16005",
                                price="16012",
                                quantity=16023,
                                sku=16042,
                                currency_code="currency code #12",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=[19001, 19002],
                            products_requiring_country=[19003, 19004],
                            products_requiring_mandatory_mark=[19005, 19006],
                            products_requiring_rnpt=[19007, 19008],
                        ),
                        status="status #1",
                        tpl_integration_type="tpl integration type #1",
                        tracking_number="142",
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
                            name="name #21",
                            phone="phone #21",
                        ),
                        analytics_data=posting_fbs_list.GetPostingFBSListResponseAnalyticsData(
                            city="city #21",
                            is_premium=True,
                            payment_type_group_name="payment type group name #21",
                            region="region #21",
                            tpl_provider="tpl provider #21",
                            tpl_provider_id=21023,
                            warehouse="warehouse #21",
                            warehouse_id=21042,
                            delivery_date_begin=datetime.datetime.fromisoformat(
                                "2006-01-04T01:04:05.999999+07:00",
                            ),
                        ),
                        barcodes=posting_fbs_list.GetPostingFBSListResponseBarcodes(
                            lower_barcode="lower barcode #21",
                            upper_barcode="upper barcode #21",
                        ),
                        cancellation=posting_fbs_list.GetPostingFBSListResponseCancellation(
                            affect_cancellation_rating=True,
                            cancel_reason="cancel reason #21",
                            cancel_reason_id=22023,
                            cancellation_initiator="cancellation initiator #21",
                            cancellation_type="cancellation type #21",
                            cancelled_after_ship=True,
                        ),
                        customer=posting_fbs_list.GetPostingFBSListResponseCustomer(
                            address=posting_fbs_list.GetPostingFBSListResponseAddress(
                                address_tail="address tail #21",
                                city="city #22",
                                comment="comment #21",
                                country="country #21",
                                district="district #21",
                                latitude=21.01,
                                longitude=21.02,
                                provider_pvz_code="provider pvz code #21",
                                pvz_code=23042,
                                region="region #21",
                                zip_code="zip code #21",
                            ),
                            customer_email="customer email #21",
                            customer_id=23023,
                            name="name #22",
                            phone="phone #22",
                        ),
                        delivery_method=posting_fbs_list.GetPostingFBSListResponseDeliveryMethod(
                            id=24012,
                            name="name #23",
                            tpl_provider="tpl provider #22",
                            tpl_provider_id=24023,
                            warehouse="warehouse #22",
                            warehouse_id=24042,
                        ),
                        financial_data=posting_fbs_list.GetPostingFBSListResponseFinancialData(
                            posting_services=\
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                    marketplace_service_item_deliv_to_customer=21.03,
                                    marketplace_service_item_direct_flow_trans=21.04,
                                    marketplace_service_item_dropoff_ff=21.05,
                                    marketplace_service_item_dropoff_pvz=21.06,
                                    marketplace_service_item_dropoff_sc=21.07,
                                    marketplace_service_item_fulfillment=21.08,
                                    marketplace_service_item_pickup=21.09,
                                    marketplace_service_item_return_after_deliv_to_customer=21.10,
                                    marketplace_service_item_return_flow_trans=21.11,
                                    marketplace_service_item_return_not_deliv_to_customer=21.12,
                                    marketplace_service_item_return_part_goods_customer=21.13,
                                ),
                            products=[
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=["action #5", "action #6"],
                                    client_price="27005",
                                    commission_amount=21.14,
                                    commission_percent=27012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=21.20,
                                            marketplace_service_item_direct_flow_trans=21.21,
                                            marketplace_service_item_dropoff_ff=21.22,
                                            marketplace_service_item_dropoff_pvz=21.23,
                                            marketplace_service_item_dropoff_sc=21.24,
                                            marketplace_service_item_fulfillment=21.25,
                                            marketplace_service_item_pickup=21.26,
                                            marketplace_service_item_return_after_deliv_to_customer=21.27,
                                            marketplace_service_item_return_flow_trans=21.28,
                                            marketplace_service_item_return_not_deliv_to_customer=21.29,
                                            marketplace_service_item_return_part_goods_customer=21.30,
                                        ),
                                    old_price=21.15,
                                    payout=21.16,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=21.31,
                                        tag="tag #21",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-03T21:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=21.17,
                                    product_id=27023,
                                    quantity=27042,
                                    total_discount_percent=21.18,
                                    total_discount_value=21.19,
                                ),
                                posting_fbs_list.GetPostingFBSListResponseFinancialDataProduct(
                                    actions=["action #7", "action #8"],
                                    client_price="28005",
                                    commission_amount=21.32,
                                    commission_percent=28012,
                                    item_services=\
                                        posting_fbs_list.GetPostingFBSListResponseFinancialDataServices(
                                            marketplace_service_item_deliv_to_customer=21.38,
                                            marketplace_service_item_direct_flow_trans=21.39,
                                            marketplace_service_item_dropoff_ff=21.40,
                                            marketplace_service_item_dropoff_pvz=21.41,
                                            marketplace_service_item_dropoff_sc=21.42,
                                            marketplace_service_item_fulfillment=21.43,
                                            marketplace_service_item_pickup=21.44,
                                            marketplace_service_item_return_after_deliv_to_customer=21.45,
                                            marketplace_service_item_return_flow_trans=21.46,
                                            marketplace_service_item_return_not_deliv_to_customer=21.47,
                                            marketplace_service_item_return_part_goods_customer=21.48,
                                        ),
                                    old_price=21.33,
                                    payout=21.34,
                                    picking=posting_fbs_list.GetPostingFBSListResponsePicking(
                                        amount=21.49,
                                        tag="tag #22",
                                        moment=datetime.datetime.fromisoformat(
                                            "2006-01-03T23:04:05.999999+07:00",
                                        ),
                                    ),
                                    price=21.35,
                                    product_id=28023,
                                    quantity=28042,
                                    total_discount_percent=21.36,
                                    total_discount_value=21.37,
                                ),
                            ],
                        ),
                        is_express=True,
                        order_id=205,
                        order_number="212",
                        posting_number="223",
                        products=[
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #5", "mandatory mark #6"],
                                name="name #24",
                                offer_id="25005",
                                price="25012",
                                quantity=25023,
                                sku=25042,
                                currency_code="currency code #21",
                            ),
                            posting_fbs_list.GetPostingFBSListResponseProduct(
                                mandatory_mark=["mandatory mark #7", "mandatory mark #8"],
                                name="name #25",
                                offer_id="26005",
                                price="26012",
                                quantity=26023,
                                sku=26042,
                                currency_code="currency code #22",
                            ),
                        ],
                        requirements=posting_fbs_list.GetPostingFBSListResponseRequirements(
                            products_requiring_gtd=[29001, 29002],
                            products_requiring_country=[29003, 29004],
                            products_requiring_mandatory_mark=[29005, 29006],
                            products_requiring_rnpt=[29007, 29008],
                        ),
                        status="status #2",
                        tpl_integration_type="tpl integration type #2",
                        tracking_number="242",
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
                has_next=True,
            ),
        ),
    ),

    # posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResultWrapper(
            result=[
                posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResult(
                    name="name #1",
                    country_iso_code="US",
                ),
                posting_fbs_product_country_list.GetPostingFBSProductCountryListResponseResult(
                    name="name #2",
                    country_iso_code="DE",
                ),
            ],
        ),
    ),

    # posting_fbs_product_country_set.GetCountrySetFBSResponseResult
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_product_country_set.GetCountrySetFBSResponseResult(
            product_id=23,
            is_gtd_needed=True,
        ),
    ),

    # posting_fbs_ship_gtd.CreatePostingFBSShipWithGTDResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=posting_fbs_ship_gtd.CreatePostingFBSShipWithGTDResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=posting_fbs_ship_gtd.CreatePostingFBSShipWithGTDResponseResultWrapper(
            result=["one", "two"],
        ),
    ),

    # product_description.GetProductInfoDescriptionResponseResultWrapper
    _ResponseTestCase(
        kind="full",
        expected_data=product_description.GetProductInfoDescriptionResponseResultWrapper(
            result=product_description.GetProductInfoDescriptionResponseResult(
                description="description",
                id=23,
                name="name",
                offer_id="42",
            ),
        ),
    ),

    # product_import_prices.GetProductImportPriceResponseResultWrapper
    _ResponseTestCase(
        kind="top_level_empty_list",
        expected_data=product_import_prices.GetProductImportPriceResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=product_import_prices.GetProductImportPriceResponseResultWrapper(
            result=[
                product_import_prices.GetProductImportPriceResponseResult(
                    errors=[],
                    offer_id="123",
                    product_id=142,
                    updated=True,
                ),
                product_import_prices.GetProductImportPriceResponseResult(
                    errors=[],
                    offer_id="223",
                    product_id=242,
                    updated=True,
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=product_import_prices.GetProductImportPriceResponseResultWrapper(
            result=[
                product_import_prices.GetProductImportPriceResponseResult(
                    errors=[
                        product_import_prices.GetProductImportPriceResponseError(
                            code="code #1",
                            message="message #1",
                        ),
                        product_import_prices.GetProductImportPriceResponseError(
                            code="code #2",
                            message="message #2",
                        ),
                    ],
                    offer_id="123",
                    product_id=142,
                    updated=True,
                ),
                product_import_prices.GetProductImportPriceResponseResult(
                    errors=[
                        product_import_prices.GetProductImportPriceResponseError(
                            code="code #3",
                            message="message #3",
                        ),
                        product_import_prices.GetProductImportPriceResponseError(
                            code="code #4",
                            message="message #4",
                        ),
                    ],
                    offer_id="223",
                    product_id=242,
                    updated=True,
                ),
            ],
        ),
    ),

    # product_import_stocks.ProductsStocksResponseProcessResultWrapper
    _ResponseTestCase(
        kind="top_level_empty_list",
        expected_data=product_import_stocks.ProductsStocksResponseProcessResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=product_import_stocks.ProductsStocksResponseProcessResultWrapper(
            result=[
                product_import_stocks.ProductsStocksResponseProcessResult(
                    errors=[],
                    offer_id="112",
                    product_id=123,
                    updated=False,
                    warehouse_id=142,
                ),
                product_import_stocks.ProductsStocksResponseProcessResult(
                    errors=[],
                    offer_id="212",
                    product_id=223,
                    updated=True,
                    warehouse_id=242,
                ),
            ],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=product_import_stocks.ProductsStocksResponseProcessResultWrapper(
            result=[
                product_import_stocks.ProductsStocksResponseProcessResult(
                    errors=[
                        product_import_stocks.ProductImportProductsStocksResponseError(
                            code="code #1",
                            message="message #1",
                        ),
                        product_import_stocks.ProductImportProductsStocksResponseError(
                            code="code #2",
                            message="message #2",
                        ),
                    ],
                    offer_id="112",
                    product_id=123,
                    updated=False,
                    warehouse_id=142,
                ),
                product_import_stocks.ProductsStocksResponseProcessResult(
                    errors=[
                        product_import_stocks.ProductImportProductsStocksResponseError(
                            code="code #3",
                            message="message #3",
                        ),
                        product_import_stocks.ProductImportProductsStocksResponseError(
                            code="code #4",
                            message="message #4",
                        ),
                    ],
                    offer_id="212",
                    product_id=223,
                    updated=True,
                    warehouse_id=242,
                ),
            ],
        ),
    ),

    # product_info_attributes.GetProductAttributesResponseResultWrapper
    _ResponseTestCase(
        kind="first_level_empty_list",
        expected_data=product_info_attributes.GetProductAttributesResponseResultWrapper(
            result=[],
            last_id="123",
            total=142,
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=product_info_attributes.GetProductAttributesResponseResultWrapper(
            result=[
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[],
                    barcode="barcode #11",
                    barcodes=[],
                    description_category_id=1005,
                    color_image="color image #11",
                    complex_attributes=[],
                    depth=1012,
                    dimension_unit="dimension unit #11",
                    height=1023,
                    id=1042,
                    images=[],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=10023,
                        count=10042,
                    ),
                    name="name #11",
                    offer_id="2005",
                    pdf_list=[],
                    primary_image="primary image #11",
                    sku=2012,
                    type_id=2023,
                    weight=2042,
                    weight_unit="weight unit #11",
                    width=3005,
                ),
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[],
                    barcode="barcode #21",
                    barcodes=[],
                    description_category_id=4005,
                    color_image="color image #21",
                    complex_attributes=[],
                    depth=4012,
                    dimension_unit="dimension unit #21",
                    height=4023,
                    id=4042,
                    images=[],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=20023,
                        count=20042,
                    ),
                    name="name #21",
                    offer_id="5005",
                    pdf_list=[],
                    primary_image="primary image #21",
                    sku=5012,
                    type_id=5023,
                    weight=5042,
                    weight_unit="weight unit #21",
                    width=6005,
                ),
            ],
            last_id="123",
            total=142,
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty_list",
        expected_data=product_info_attributes.GetProductAttributesResponseResultWrapper(
            result=[
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=100023,
                            complex_id=100042,
                            values=[],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=200023,
                            complex_id=200042,
                            values=[],
                        ),
                    ],
                    barcode="barcode #11",
                    barcodes=["barcode #1", "barcode #2"],
                    description_category_id=1005,
                    color_image="color image #11",
                    complex_attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=300023,
                            complex_id=300042,
                            values=[],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=400023,
                            complex_id=400042,
                            values=[],
                        ),
                    ],
                    depth=1012,
                    dimension_unit="dimension unit #11",
                    height=1023,
                    id=1042,
                    images=["image #1", "image #2"],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=10023,
                        count=10042,
                    ),
                    name="name #11",
                    offer_id="2005",
                    pdf_list=[
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #11",
                            name="name #12",
                        ),
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #12",
                            name="name #13",
                        ),
                    ],
                    primary_image="primary image #11",
                    sku=2012,
                    type_id=2023,
                    weight=2042,
                    weight_unit="weight unit #11",
                    width=3005,
                ),
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=500023,
                            complex_id=500042,
                            values=[],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=600023,
                            complex_id=600042,
                            values=[],
                        ),
                    ],
                    barcode="barcode #21",
                    barcodes=["barcode #3", "barcode #4"],
                    description_category_id=4005,
                    color_image="color image #21",
                    complex_attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=700023,
                            complex_id=700042,
                            values=[],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=800023,
                            complex_id=800042,
                            values=[],
                        ),
                    ],
                    depth=4012,
                    dimension_unit="dimension unit #21",
                    height=4023,
                    id=4042,
                    images=["image #3", "image #4"],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=20023,
                        count=20042,
                    ),
                    name="name #21",
                    offer_id="5005",
                    pdf_list=[
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #21",
                            name="name #22",
                        ),
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #22",
                            name="name #23",
                        ),
                    ],
                    primary_image="primary image #21",
                    sku=5012,
                    type_id=5023,
                    weight=5042,
                    weight_unit="weight unit #21",
                    width=6005,
                ),
            ],
            last_id="123",
            total=142,
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=product_info_attributes.GetProductAttributesResponseResultWrapper(
            result=[
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=100023,
                            complex_id=100042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=1000023,
                                    value="value #11",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=2000023,
                                    value="value #12",
                                ),
                            ],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=200023,
                            complex_id=200042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=3000023,
                                    value="value #13",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=4000023,
                                    value="value #14",
                                ),
                            ],
                        ),
                    ],
                    barcode="barcode #11",
                    barcodes=["barcode #1", "barcode #2"],
                    description_category_id=1005,
                    color_image="color image #11",
                    complex_attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=300023,
                            complex_id=300042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=5000023,
                                    value="value #15",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=6000023,
                                    value="value #16",
                                ),
                            ],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=400023,
                            complex_id=400042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=7000023,
                                    value="value #17",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=8000023,
                                    value="value #18",
                                ),
                            ],
                        ),
                    ],
                    depth=1012,
                    dimension_unit="dimension unit #11",
                    height=1023,
                    id=1042,
                    images=["image #1", "image #2"],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=10023,
                        count=10042,
                    ),
                    name="name #11",
                    offer_id="2005",
                    pdf_list=[
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #11",
                            name="name #12",
                        ),
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #12",
                            name="name #13",
                        ),
                    ],
                    primary_image="primary image #11",
                    sku=2012,
                    type_id=2023,
                    weight=2042,
                    weight_unit="weight unit #11",
                    width=3005,
                ),
                product_info_attributes.GetProductAttributesResponseResult(
                    attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=500023,
                            complex_id=500042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=9000023,
                                    value="value #21",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=10000023,
                                    value="value #22",
                                ),
                            ],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=600023,
                            complex_id=600042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=11000023,
                                    value="value #23",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=12000023,
                                    value="value #24",
                                ),
                            ],
                        ),
                    ],
                    barcode="barcode #21",
                    barcodes=["barcode #3", "barcode #4"],
                    description_category_id=4005,
                    color_image="color image #21",
                    complex_attributes=[
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=700023,
                            complex_id=700042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=13000023,
                                    value="value #25",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=14000023,
                                    value="value #26",
                                ),
                            ],
                        ),
                        product_info_attributes.GetProductAttributesResponseAttribute(
                            id=800023,
                            complex_id=800042,
                            values=[
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=15000023,
                                    value="value #27",
                                ),
                                product_info_attributes.GetProductAttributesDictionaryValue(
                                    dictionary_value_id=16000023,
                                    value="value #28",
                                ),
                            ],
                        ),
                    ],
                    depth=4012,
                    dimension_unit="dimension unit #21",
                    height=4023,
                    id=4042,
                    images=["image #3", "image #4"],
                    model_info=product_info_attributes.GetProductModelInfoValue(
                        model_id=20023,
                        count=20042,
                    ),
                    name="name #21",
                    offer_id="5005",
                    pdf_list=[
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #21",
                            name="name #22",
                        ),
                        product_info_attributes.GetProductAttributesPdf(
                            file_name="file name #22",
                            name="name #23",
                        ),
                    ],
                    primary_image="primary image #21",
                    sku=5012,
                    type_id=5023,
                    weight=5042,
                    weight_unit="weight unit #21",
                    width=6005,
                ),
            ],
            last_id="123",
            total=142,
        ),
    ),

    # product_info.GetProductInfoResponseResultWrapper
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=product_info.GetProductInfoResponseResultWrapper(
            result=product_info.GetProductInfoResponseResult(
                barcode="barcode",
                buybox_price="1.01",
                category_id=105,
                color_image="color image",
                commissions=[],
                fbo_sku=112,
                fbs_sku=123,
                id=142,
                images=[],
                primary_image="primary image",
                images360=[],
                is_prepayment=False,
                is_prepayment_allowed=False,
                marketing_price="1.02",
                min_ozon_price="1.03",
                min_price="1.04",
                name="name",
                offer_id="205",
                old_price="1.05",
                premium_price="1.06",
                price="1.07",
                price_index="212",
                recommended_price="1.08",
                status=product_info.GetProductInfoResponseStatus(
                    state="state",
                    state_failed="state failed",
                    moderate_status="moderate status",
                    decline_reasons=[],
                    validation_state="validation state",
                    state_name="state name",
                    state_description="state description",
                    is_failed=False,
                    is_created=False,
                    state_tooltip="state tooltip",
                    item_errors=[],
                    state_updated_at=datetime.datetime.fromisoformat(
                        "2006-01-02T17:04:05.999999+07:00",
                    ),
                ),
                sources=[],
                stocks=product_info.GetProductInfoResponseStocks(
                    coming=223,
                    present=242,
                    reserved=305,
                ),
                vat="vat",
                visibility_details=product_info.GetProductInfoResponseVisibilityDetails(
                    active_product=False,
                    has_price=False,
                    has_stock=False,
                ),
                visible=False,
                volume_weight=1.09,
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
            ),
        ),
    ),
    _ResponseTestCase(
        kind="third_level_empty_list",
        expected_data=product_info.GetProductInfoResponseResultWrapper(
            result=product_info.GetProductInfoResponseResult(
                barcode="barcode",
                buybox_price="1.01",
                category_id=105,
                color_image="color image",
                commissions=[
                    product_info.GetProductInfoResponseCommissions(
                        delivery_amount=1.10,
                        min_value=1.11,
                        percent=1.12,
                        return_amount=1.13,
                        sale_schema="sale schema #1",
                        value=1.14,
                    ),
                    product_info.GetProductInfoResponseCommissions(
                        delivery_amount=1.15,
                        min_value=1.16,
                        percent=1.17,
                        return_amount=1.18,
                        sale_schema="sale schema #2",
                        value=1.19,
                    ),
                ],
                fbo_sku=112,
                fbs_sku=123,
                id=142,
                images=["image #1", "image #2"],
                primary_image="primary image",
                images360=["image 360 #1", "image 360 #2"],
                is_prepayment=True,
                is_prepayment_allowed=True,
                marketing_price="1.02",
                min_ozon_price="1.03",
                min_price="1.04",
                name="name",
                offer_id="205",
                old_price="1.05",
                premium_price="1.06",
                price="1.07",
                price_index="212",
                recommended_price="1.08",
                status=product_info.GetProductInfoResponseStatus(
                    state="state",
                    state_failed="state failed",
                    moderate_status="moderate status",
                    decline_reasons=["decline reason #1", "decline reason #2"],
                    validation_state="validation state",
                    state_name="state name",
                    state_description="state description",
                    is_failed=True,
                    is_created=True,
                    state_tooltip="state tooltip",
                    item_errors=[
                        product_info.GetProductInfoResponseItemError(
                            code="code #1",
                            state="state #1",
                            level="level #1",
                            description="description #1",
                            field="field #1",
                            attribute_id="312",
                            attribute_name="attribute name #1",
                            optional_description_elements=\
                                product_info.GetProductInfoResponseOptionalDescriptionElements(
                                    properties={},
                                ),
                        ),
                        product_info.GetProductInfoResponseItemError(
                            code="code #2",
                            state="state #2",
                            level="level #2",
                            description="description #2",
                            field="field #2",
                            attribute_id="323",
                            attribute_name="attribute name #2",
                            optional_description_elements=\
                                product_info.GetProductInfoResponseOptionalDescriptionElements(
                                    properties={},
                                ),
                        ),
                    ],
                    state_updated_at=datetime.datetime.fromisoformat(
                        "2006-01-02T17:04:05.999999+07:00",
                    ),
                ),
                sources=[
                    product_info.GetProductInfoResponseSource(
                        is_enabled=False,
                        sku=342,
                        source="source #1",
                    ),
                    product_info.GetProductInfoResponseSource(
                        is_enabled=True,
                        sku=405,
                        source="source #2",
                    ),
                ],
                stocks=product_info.GetProductInfoResponseStocks(
                    coming=223,
                    present=242,
                    reserved=305,
                ),
                vat="vat",
                visibility_details=product_info.GetProductInfoResponseVisibilityDetails(
                    active_product=True,
                    has_price=True,
                    has_stock=True,
                ),
                visible=True,
                volume_weight=1.09,
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=product_info.GetProductInfoResponseResultWrapper(
            result=product_info.GetProductInfoResponseResult(
                barcode="barcode",
                buybox_price="1.01",
                category_id=105,
                color_image="color image",
                commissions=[
                    product_info.GetProductInfoResponseCommissions(
                        delivery_amount=1.10,
                        min_value=1.11,
                        percent=1.12,
                        return_amount=1.13,
                        sale_schema="sale schema #1",
                        value=1.14,
                    ),
                    product_info.GetProductInfoResponseCommissions(
                        delivery_amount=1.15,
                        min_value=1.16,
                        percent=1.17,
                        return_amount=1.18,
                        sale_schema="sale schema #2",
                        value=1.19,
                    ),
                ],
                fbo_sku=112,
                fbs_sku=123,
                id=142,
                images=["image #1", "image #2"],
                primary_image="primary image",
                images360=["image 360 #1", "image 360 #2"],
                is_prepayment=True,
                is_prepayment_allowed=True,
                marketing_price="1.02",
                min_ozon_price="1.03",
                min_price="1.04",
                name="name",
                offer_id="205",
                old_price="1.05",
                premium_price="1.06",
                price="1.07",
                price_index="212",
                recommended_price="1.08",
                status=product_info.GetProductInfoResponseStatus(
                    state="state",
                    state_failed="state failed",
                    moderate_status="moderate status",
                    decline_reasons=["decline reason #1", "decline reason #2"],
                    validation_state="validation state",
                    state_name="state name",
                    state_description="state description",
                    is_failed=True,
                    is_created=True,
                    state_tooltip="state tooltip",
                    item_errors=[
                        product_info.GetProductInfoResponseItemError(
                            code="code #1",
                            state="state #1",
                            level="level #1",
                            description="description #1",
                            field="field #1",
                            attribute_id="312",
                            attribute_name="attribute name #1",
                            optional_description_elements=\
                                product_info.GetProductInfoResponseOptionalDescriptionElements(
                                    properties={
                                        "unexpected_key": "unexpected value",
                                        "key #1": "value #1",
                                        "key #2": "value #2",
                                    },
                                ),
                        ),
                        product_info.GetProductInfoResponseItemError(
                            code="code #2",
                            state="state #2",
                            level="level #2",
                            description="description #2",
                            field="field #2",
                            attribute_id="323",
                            attribute_name="attribute name #2",
                            optional_description_elements=\
                                product_info.GetProductInfoResponseOptionalDescriptionElements(
                                    properties={
                                        "unexpected_key": "unexpected value",
                                        "key #3": "value #3",
                                        "key #4": "value #4",
                                    },
                                ),
                        ),
                    ],
                    state_updated_at=datetime.datetime.fromisoformat(
                        "2006-01-02T17:04:05.999999+07:00",
                    ),
                ),
                sources=[
                    product_info.GetProductInfoResponseSource(
                        is_enabled=False,
                        sku=342,
                        source="source #1",
                    ),
                    product_info.GetProductInfoResponseSource(
                        is_enabled=True,
                        sku=405,
                        source="source #2",
                    ),
                ],
                stocks=product_info.GetProductInfoResponseStocks(
                    coming=223,
                    present=242,
                    reserved=305,
                ),
                vat="vat",
                visibility_details=product_info.GetProductInfoResponseVisibilityDetails(
                    active_product=True,
                    has_price=True,
                    has_stock=True,
                ),
                visible=True,
                volume_weight=1.09,
                created_at=datetime.datetime.fromisoformat(
                    "2006-01-02T15:04:05.999999+07:00",
                ),
            ),
        ),
    ),

    # product_pictures_import.ProductPicturesResponseResultWrapper
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=product_pictures_import.ProductPicturesResponseResultWrapper(
            result=product_pictures_import.ProductPicturesResponseResult(
                pictures=[],
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=product_pictures_import.ProductPicturesResponseResultWrapper(
            result=product_pictures_import.ProductPicturesResponseResult(
                pictures=[
                    product_pictures_import.ProductPicturesResponseResultPictures(
                        is_360=False,
                        is_color=False,
                        is_primary=False,
                        product_id=23,
                        state="state #1",
                        url="url #1",
                    ),
                    product_pictures_import.ProductPicturesResponseResultPictures(
                        is_360=True,
                        is_color=True,
                        is_primary=True,
                        product_id=42,
                        state="state #2",
                        url="url #2",
                    ),
                ],
            ),
        ),
    ),

    # products_stocks.SetProductStocksResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=products_stocks.SetProductStocksResponseResultWrapper(
            result=[],
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=products_stocks.SetProductStocksResponseResultWrapper(
            result=[
                products_stocks.SetProductStocksResponseResult(
                    offer_id="112",
                    product_id=123,
                    updated=True,
                    warehouse_id=142,
                ),
                products_stocks.SetProductStocksResponseResult(
                    offer_id="212",
                    product_id=223,
                    updated=True,
                    warehouse_id=242,
                ),
            ],
        ),
    ),

    # returns_fbo.GetReturnsCompanyFBOResponseResult
    _ResponseTestCase(
        kind="empty_list",
        expected_data=returns_fbo.GetReturnsCompanyFBOResponseResult(
            returns=[],
            count=0,
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=returns_fbo.GetReturnsCompanyFBOResponseResult(
            returns=[
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
            ],
            count=100,
        ),
    ),

    # returns_fbs.GetReturnsCompanyFBSResponseResultWrapper
    _ResponseTestCase(
        kind="empty_list",
        expected_data=returns_fbs.GetReturnsCompanyFBSResponseResultWrapper(
            result=returns_fbs.GetReturnsCompanyFBSResponseResult(
                returns=[],
                count=0,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="nulls",
        expected_data=returns_fbs.GetReturnsCompanyFBSResponseResultWrapper(
            result=returns_fbs.GetReturnsCompanyFBSResponseResult(
                returns=[
                    returns_fbs.GetReturnsCompanyFBSResponseItem(
                        accepted_from_customer_moment=None,
                        clearing_id=None,
                        commission=None,
                        commission_percent=None,
                        id=None,
                        is_moving=None,
                        is_opened=None,
                        last_free_waiting_day=None,
                        place_id=None,
                        moving_to_place_name=None,
                        picking_amount=None,
                        posting_number=None,
                        price=None,
                        price_without_commission=None,
                        product_id=None,
                        product_name=None,
                        quantity=None,
                        return_date=None,
                        return_reason_name=None,
                        waiting_for_seller_date_time=None,
                        returned_to_seller_date_time=None,
                        waiting_for_seller_days=None,
                        returns_keeping_cost=None,
                        sku=None,
                        status=None,
                    ),
                    returns_fbs.GetReturnsCompanyFBSResponseItem(
                        accepted_from_customer_moment=None,
                        clearing_id=None,
                        commission=None,
                        commission_percent=None,
                        id=None,
                        is_moving=None,
                        is_opened=None,
                        last_free_waiting_day=None,
                        place_id=None,
                        moving_to_place_name=None,
                        picking_amount=None,
                        posting_number=None,
                        price=None,
                        price_without_commission=None,
                        product_id=None,
                        product_name=None,
                        quantity=None,
                        return_date=None,
                        return_reason_name=None,
                        waiting_for_seller_date_time=None,
                        returned_to_seller_date_time=None,
                        waiting_for_seller_days=None,
                        returns_keeping_cost=None,
                        sku=None,
                        status=None,
                    ),
                ],
                count=100,
            ),
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=returns_fbs.GetReturnsCompanyFBSResponseResultWrapper(
            result=returns_fbs.GetReturnsCompanyFBSResponseResult(
                returns=[
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
                ],
                count=100,
            ),
        ),
    ),

    # stocks.GetProductInfoStocksResponseResult
    _ResponseTestCase(
        kind="top_level_empty_list",
        expected_data=stocks.GetProductInfoStocksResponseResult(
            cursor="23",
            items=[],
            total=42,
        ),
    ),
    _ResponseTestCase(
        kind="second_level_empty_list",
        expected_data=stocks.GetProductInfoStocksResponseResult(
            cursor="23",
            items=[
                stocks.GetProductInfoStocksResponseItem(
                    offer_id="123",
                    product_id=142,
                    stocks=[],
                ),
                stocks.GetProductInfoStocksResponseItem(
                    offer_id="223",
                    product_id=242,
                    stocks=[],
                ),
            ],
            total=42,
        ),
    ),
    _ResponseTestCase(
        kind="full",
        expected_data=stocks.GetProductInfoStocksResponseResult(
            cursor="23",
            items=[
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
            ],
            total=42,
        ),
    ),
]


class TestResponses(unittest.TestCase):
    def test_responses(self) -> None:
        for test_case in _RESPONSES_TEST_CASES:
            data_name = common.get_full_qualified_name(test_case.expected_data)
            test_case_name = f"{data_name} [{test_case.kind}]"

            with self.subTest(test_case_name):
                input_json_filename = f"{test_case.kind}.json"
                input_json_path = _TEST_DATA_PATH.joinpath(
                    common.get_last_module(test_case.expected_data),
                    common.get_qualified_name(test_case.expected_data),
                    input_json_filename,
                )

                with open(input_json_path) as input_json_file:
                    input_json = input_json_file.read().strip()

                data_cls = test_case.expected_data.__class__
                actual_data = data_cls.schema().loads(input_json, many=None)

                self.assertEqual(test_case.expected_data, actual_data)
