import datetime

from functools import wraps
from ice3x.exceptions import UnauthorisedResourceException


def requires_authentication(func):
    """Helper function to protect unauthenticated use of private resources"""

    @wraps(func)
    def inner(self, *args, **kwargs):
        if not self._has_auth_details:
            raise UnauthorisedResourceException(
                f"authentication is required for private resources"
            )

        return func(self, *args, **kwargs)

    return inner


def add_nonce(func):
    """Helper function which adds a nonce to the kwargs dict"""

    @wraps(func)
    def inner(*args, **kwargs):
<<<<<<< HEAD
        if "nonce" not in kwargs:
            kwargs["nonce"] = int(datetime.datetime.utcnow().timestamp())

=======
        if 'nonce' not in kwargs:
            kwargs['nonce'] = int(datetime.datetime.utcnow().timestamp() * 1000)
            
>>>>>>> af82590187a6c2bb6aedc5b29a10329decb19b08
        return func(*args, **kwargs)

    return inner
