import pytest
import requests_mock

from ice3x.clients.sync import IceCubedSyncClient


@pytest.fixture
def client():
    return IceCubedSyncClient('api_key', 'secret')


def test_get_public_trade_info(client) -> None:
    """Test the get_public_trade_info of the sync client"""

    url = f'{IceCubedSyncClient.BASE_URL}/trade/info'
    
    data = {
        'errors': False,
        'response': {'entity': {'created': '1516294139',
        'pair_id': '6',
        'price': '2805.01000000',
        'trade_id': '1437296',
        'type': 'buy',
        'volume': 1.98479306}}
    }

    with requests_mock.mock() as m:
        m.get(url, json=data)
        response = client.get_public_trade_info(trade_id=1)
        
        message = (f"expected reponse {data}, received {response}")
        assert data == response, message