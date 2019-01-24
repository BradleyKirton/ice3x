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
def response():
    """Provides a response object as a fixture"""
    return Response()


def test_get_public_trade_info(mocker, response, client) -> None:
    """Test the get_public_trade_info of the sync client"""
    url = f"{IceCubedSyncClient.BASE_URI}trade/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_public_trade_info(trade_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_public_trade_list(mocker, response, client) -> None:
    """Test the test_get_public_trade_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}trade/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_public_trade_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_market_depth(mocker, response, client) -> None:
    """Test the get_market_depth of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}stats/marketdepth"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_market_depth()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_pair_info(mocker, response, client) -> None:
    """Test the get_pair_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}pair/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_pair_info(pair_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_pair_list(mocker, response, client) -> None:
    """Test the get_pair_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}pair/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_pair_list(pair_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_currency_info(mocker, response, client) -> None:
    """Test the get_currency_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}currency/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_currency_info(currency_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_currency_list(mocker, response, client) -> None:
    """Test the get_currency_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}currency/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_currency_list(currency_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_orderbook_info(mocker, response, client) -> None:
    """Test the get_orderbook_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}orderbook/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_orderbook_info(pair_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_market_depth_full(mocker, response, client) -> None:
    """Test the get_orderbook_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}stats/marketdepthfull"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_market_depth_full()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_market_depth_bt_cav(mocker, response, client) -> None:
    """Test the get_market_depth_bt_cav of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}stats/marketdepthbtcav"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_market_depth_bt_cav()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_invoice_list(mocker, response, client) -> None:
    """Test the get_invoice_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}invoice/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_invoice_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_invoice_info(mocker, response, client) -> None:
    """Test the get_invoice_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}invoice/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_invoice_info(invoice_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_invoice_pdf(mocker, response, client) -> None:
    """Test the get_invoice_pdf of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}invoice/pdf"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_invoice_pdf(invoice_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_cancel_order(mocker, response, client) -> None:
    """Test the cancel_order of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}order/cancel"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.cancel_order(order_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_create_order(mocker, response, client) -> None:
    """Test the create_order of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}order/new"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.create_order(pair_id=1, amount=100, kind="buy", price=100)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_order_info(mocker, response, client) -> None:
    """Test the get_order_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}order/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_order_info(order_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_order_list(mocker, response, client) -> None:
    """Test the get_order_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}order/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_order_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_transaction_info(mocker, response, client) -> None:
    """Test the get_transaction_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}transaction/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_transaction_info(transaction_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_transaction_list(mocker, response, client) -> None:
    """Test the get_transaction_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}transaction/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_transaction_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_trade_info(mocker, response, client) -> None:
    """Test the get_trade_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}trade/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_trade_info(trade_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_trade_list(mocker, response, client) -> None:
    """Test the get_trade_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}trade/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_trade_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_balance_list(mocker, response, client) -> None:
    """Test the get_balance_list of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}balance/list"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_balance_list()

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_get_balance_info(mocker, response, client) -> None:
    """Test the get_balance_info of the sync client"""

    url = f"{IceCubedSyncClient.BASE_URI}balance/info"
    data = {}

    mocker.patch("requests.Session.request", return_value=response)
    response = client.get_balance_info(currency_id=1)

    message = f"expected reponse {data}, received {response}"
    assert data == response, message


def test_unauthorised_access(mocker, response, uclient):
    """Test that the requires_authentication throws an error when accessing a resource without authentication"""

    url = f"{IceCubedSyncClient.BASE_URI}balance/info"
    data = {}

    with pytest.raises(UnauthorisedResourceException):
        mocker.patch("requests.Session.request", return_value=response)
        response = uclient.get_balance_info(currency_id=1)
