from unittest.mock import Mock

import pytest
from ice3x.clients.sync import IceCubedSyncClient
from ice3x.exceptions import UnauthorisedResourceException


class Response:
    def raise_for_status(self) -> None:
        pass

    def json(self):
        return {}


@pytest.fixture
def client():
    """Provides an authorized client as a fixture"""
    return IceCubedSyncClient("api_key", "secret")


@pytest.fixture
def uclient():
    """Provides an unauthorized client as a fixture"""
    return IceCubedSyncClient()


@pytest.fixture
def expected_data():
    return {}


@pytest.fixture
def expected_response(expected_data):
    """Provides an expected response."""

    response = Mock()
    response.json.return_value = expected_data
    return response


def test_get_public_trade_info(
    mocker, expected_response, expected_data, client
) -> None:
    """Test the get_public_trade_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_public_trade_info(trade_id=1)

    assert actual_data == expected_data


def test_get_public_trade_list(
    mocker, expected_response, expected_data, client
) -> None:
    """Test the test_get_public_trade_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_public_trade_list()

    assert actual_data == expected_data


def test_get_market_depth(mocker, expected_response, expected_data, client) -> None:
    """Test the get_market_depth of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_market_depth()

    assert actual_data == expected_data


def test_get_pair_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_pair_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_pair_info(pair_id=1)

    assert actual_data == expected_data


def test_get_pair_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_pair_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_pair_list(pair_id=1)

    assert actual_data == expected_data


def test_get_currency_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_currency_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_currency_info(currency_id=1)

    assert actual_data == expected_data


def test_get_currency_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_currency_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_currency_list(currency_id=1)

    assert actual_data == expected_data


def test_get_orderbook_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_orderbook_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_orderbook_info(pair_id=1)

    assert actual_data == expected_data


def test_get_market_depth_full(
    mocker, expected_response, expected_data, client
) -> None:
    """Test the get_orderbook_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_market_depth_full()

    assert actual_data == expected_data


def test_get_market_depth_bt_cav(
    mocker, expected_response, expected_data, client
) -> None:
    """Test the get_market_depth_bt_cav of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_market_depth_bt_cav()

    assert actual_data == expected_data


def test_get_invoice_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_invoice_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_invoice_list()

    assert actual_data == expected_data


def test_get_invoice_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_invoice_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_invoice_info(invoice_id=1)

    assert actual_data == expected_data


def test_get_invoice_pdf(mocker, expected_response, expected_data, client) -> None:
    """Test the get_invoice_pdf of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_invoice_pdf(invoice_id=1)

    assert actual_data == expected_data


def test_cancel_order(mocker, expected_response, expected_data, client) -> None:
    """Test the cancel_order of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.cancel_order(order_id=1)

    assert actual_data == expected_data


def test_create_order(mocker, expected_response, expected_data, client) -> None:
    """Test the create_order of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.create_order(pair_id=1, amount=100, kind="buy", price=100)

    assert actual_data == expected_data


def test_get_order_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_order_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_order_info(order_id=1)

    assert actual_data == expected_data


def test_get_order_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_order_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_order_list()

    assert actual_data == expected_data


def test_get_transaction_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_transaction_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_transaction_info(transaction_id=1)

    assert actual_data == expected_data


def test_get_transaction_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_transaction_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_transaction_list()

    assert actual_data == expected_data


def test_get_trade_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_trade_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_trade_info(trade_id=1)

    assert actual_data == expected_data


def test_get_trade_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_trade_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_trade_list()

    assert actual_data == expected_data


def test_get_balance_list(mocker, expected_response, expected_data, client) -> None:
    """Test the get_balance_list of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_balance_list()

    assert actual_data == expected_data


def test_get_balance_info(mocker, expected_response, expected_data, client) -> None:
    """Test the get_balance_info of the sync client"""

    mocker.patch("requests.Session.request", return_value=expected_response)
    actual_data = client.get_balance_info(currency_id=1)

    assert actual_data == expected_data


def test_unauthorised_access(mocker, expected_response, uclient):
    """Test that the requires_authentication throws an error when accessing a resource without authentication"""

    with pytest.raises(UnauthorisedResourceException):
        mocker.patch("requests.Session.request", return_value=expected_response)
        uclient.get_balance_info(currency_id=1)
