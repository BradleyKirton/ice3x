import pytest
import requests_mock

from ice3x.clients.sync import IceCubedSyncClient
from ice3x.exceptions import UnauthorisedResourceException


@pytest.fixture
def client():
    """Provides an authorized client as a fixture"""
    return IceCubedSyncClient('api_key', 'secret')


@pytest.fixture
def uclient():
    """Provides an unauthorized client as a fixture"""
    return IceCubedSyncClient()


def test_get_public_trade_info(client) -> None:
    """Test the get_public_trade_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/trade/info'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_public_trade_info(trade_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_public_trade_list(client) -> None:
    """Test the test_get_public_trade_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/trade/list'
    data = {}
    
    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_public_trade_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_market_depth(client) -> None:
    """Test the get_market_depth of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/stats/marketdepth'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_market_depth()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_pair_info(client) -> None:
    """Test the get_pair_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/pair/info'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_pair_info(pair_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message



def test_get_pair_list(client) -> None:
    """Test the get_pair_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/pair/list'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_pair_list(pair_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_currency_info(client) -> None:
    """Test the get_currency_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/currency/info'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_currency_info(currency_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_currency_list(client) -> None:
    """Test the get_currency_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/currency/list'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_currency_list(currency_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_orderbook_info(client) -> None:
    """Test the get_orderbook_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/orderbook/info'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_orderbook_info(pair_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_market_depth_full(client) -> None:
    """Test the get_orderbook_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/stats/marketdepthfull'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_market_depth_full()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_market_depth_bt_cav(client) -> None:
    """Test the get_market_depth_bt_cav of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/stats/marketdepthbtcav'
    data = {}

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_market_depth_bt_cav()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_invoice_list(client) -> None:
    """Test the get_invoice_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/invoice/list'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_invoice_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_invoice_info(client) -> None:
    """Test the get_invoice_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/invoice/info'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_invoice_info(invoice_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_invoice_pdf(client) -> None:
    """Test the get_invoice_pdf of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/invoice/pdf'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_invoice_pdf(invoice_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_cancel_order(client) -> None:
    """Test the cancel_order of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/order/cancel'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.cancel_order(order_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_create_order(client) -> None:
    """Test the create_order of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/order/new'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.create_order(pair_id=1, amount=100, otype='buy')
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_order_info(client) -> None:
    """Test the get_order_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/order/info'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_order_info(order_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_order_list(client) -> None:
    """Test the get_order_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/order/list'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_order_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_transaction_info(client) -> None:
    """Test the get_transaction_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/transaction/info'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_transaction_info(transaction_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_transaction_list(client) -> None:
    """Test the get_transaction_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/transaction/list'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_transaction_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_trade_info(client) -> None:
    """Test the get_trade_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/trade/info'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_trade_info(trade_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_trade_list(client) -> None:
    """Test the get_trade_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/trade/list'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_trade_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_balance_list(client) -> None:
    """Test the get_balance_list of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/balance/list'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_balance_list()
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_get_balance_info(client) -> None:
    """Test the get_balance_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/balance/info'
    data = {}

    with requests_mock.mock() as m:
        m.post(url, json=data)
        response = client.get_balance_info(currency_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message


def test_unauthorised_access(uclient):
    """Test that the requires_authentication throws an error when accessing a resource without authentication"""

    url = f'{IceCubedSyncClient.BASE_URL}/balance/info'
    data = {}

    with pytest.raises(UnauthorisedResourceException):
        with requests_mock.mock() as m:
            m.post(url, json=data)
            response = uclient.get_balance_info(currency_id=1)