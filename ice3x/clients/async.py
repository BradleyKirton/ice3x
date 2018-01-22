import treq

from typing import Dict
from ice3x.clients.abc import IceCubedClientBase
from ice3x.decorators import add_nonce, requires_authentication
from twisted.internet.defer import Deferred
from twisted.internet.defer import inlineCallbacks


class IceCubedAsyncClient(IceCubedClientBase):
    def _get_headers(self) -> Deferred:
        return {'User-Agent': 'Mozilla/4.0 (compatible; Ice3x Async Python client)'}

    def _get_post_headers(self, signature: str) -> Deferred:
        """"""
        headers = self._get_headers()
        headers.update({'Key': self.api_key, 'Sign': signature})

        return headers

    def __init__(self, api_key: str=None, secret: str=None) -> None:
        """Instantiate the client

        Args:
            api_key: An ICE3X public API key
            secret: An ICE3X private API key
        """
        self.api_key = api_key
        self.secret = secret

    @inlineCallbacks
    def get_public_trade_info(self, trade_id: int, **params: Dict) -> Deferred:
        """Fetch public info relating to a specified trade

        Args:
            trade_id: A valid trade id

        Returns:
            Data relating to the specified trade id
        """
        url = f'{self.BASE_URL}/trade/info'
        
        params.update({'trade_id': trade_id})
        response = yield treq.get(url, params=params)
        data = yield response.json()

        return data

    @inlineCallbacks
    def get_public_trade_list(self, **params: Dict) -> Deferred:
        """Fetch a public facing list of trades

        Returns:
            A list of public trade data
        """
        url = f'{self.BASE_URL}/trade/list'

        response = yield treq.get(url, params=params)
        data = yield response.json()

        return data
    
    @inlineCallbacks
    def get_market_depth(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/stats/marketdepth'

        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
        
    @inlineCallbacks
    def get_pair_info(self, pair_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/pair/info'

        params.update({'pair_id': pair_id})
        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @inlineCallbacks
    def get_pair_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/pair/list'

        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @inlineCallbacks
    def get_currency_info(self, currency_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/currency/info'
    
        params.update({'currency_id': currency_id})
        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @inlineCallbacks
    def get_currency_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/currency/list'
    
        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data

    @inlineCallbacks
    def get_orderbook_info(self, pair_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/orderbook/info'
    
        params.update({'pair_id': pair_id})
        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data

    @inlineCallbacks
    def get_market_depth_full(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/stats/marketdepthfull'

        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @inlineCallbacks
    def get_market_depth_bt_cav(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/stats/marketdepthbtcav'

        headers = self._get_headers()
        response = yield treq.get(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_invoice_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/invoice/list'
            
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_invoice_info(self, invoice_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/invoice/info'
        
        params.update({'invoice_id': invoice_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_invoice_pdf(self, invoice_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/invoice/pdf'
        
        params.update({'invoice_id': invoice_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def cancel_order(self, order_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/order/cancel'
        
        params.update({'order_id': order_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def create_order(self, pair_id: int, amount: float, otype: str, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/order/new'
        
        params.update(
            {
                'pair_id': pair_id,
                'amount': amount,
                'type': otype
            }
        )

        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_order_info(self, order_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/order/info'
        
        params.update({'order_id': order_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_order_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/order/list'
        
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_transaction_info(self, transaction_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/transaction/info'
        
        params.update({'transaction_id': transaction_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_transaction_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/transaction/list'
        
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_trade_info(self, trade_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/trade/info'
        
        params.update({'trade_id': trade_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_trade_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/trade/list'

        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_balance_list(self, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/balance/list'

        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data
    
    @add_nonce
    @requires_authentication
    @inlineCallbacks
    def get_balance_info(self, currency_id: int, **params: Dict) -> Deferred:
        """"""
        url = f'{self.BASE_URL}/balance/info'

        params.update({'currency_id': currency_id})
        signature = self.sign(params)
        headers = self._get_post_headers(signature)
        
        response = yield treq.post(url, params=params, headers=headers)
        data = yield response.json()

        return data