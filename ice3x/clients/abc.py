import abc
import hmac
import urllib
import hashlib

from typing import Dict


class IceCubedClientABC(abc.ABC):
    BASE_URL = 'https://ice3x.com/api/v1'
    
    @abc.abstractproperty
    def _has_auth_details(self) -> bool:
        pass

    @abc.abstractmethod
    def sign(self, params: Dict) -> str:
        pass

    @abc.abstractmethod
    def _get_post_headers(self, signature: str) -> Dict:
    	pass


class IceCubedClientBase(IceCubedClientABC):
    @property
    def _has_auth_details(self) -> bool:
        """Internal helper function which checks that an API key and secret have been provided"""
        return all([self.secret is not None, self.api_key is not None])

    def _get_post_headers(self, signature: str) -> Dict:
        """"""
        return {
            'Key': self.api_key,
            'Sign': signature
        }

    def sign(self, params: Dict) -> str:
        """Sign a dict of query params for private API calls

        Args:
            params: A dict of query params

        Returns:
            A sha512 signed payload
        """
        query = urllib.parse.urlencode(params)
        signature = hmac.new(self.secret.encode(), query.encode(), hashlib.sha512)
        
        return signature.hexdigest()