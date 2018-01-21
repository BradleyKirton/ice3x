# ICE3X Python Library

This ice3x library is a Python package compliant with the ICE3X APi version 2.

This package is essentially a port of the official [PHP client](https://github.com/ICE3X/v2-PHP).

# Quickstart

The ICE3X API has two broad categories of resources, protected and unprotected resources.

In order to access protected resources one needs to create a private and public key under the [account management](https://ice3x.com/account/api) section of their platform.

Below is an example of accessing the ICE3X API with the sync client.

```python
from ice3x.clients.sync import IceCubedSyncClient

api_key = 'public key'
secret = 'private key'

client = IceCubedSyncClient(api_key=api_key, secret=secret)
client.get_public_trade_list()
```

# Installation

Clone the repo and install.

```bash
git clone https://github.com/BradleyKirton/ice3x
cd ice3x
python -m venv env # virtualenv env
source env/bin/activate
pip install .
```

# Developement

Clone the repo and install the package with it's development requirements.

```bash
git clone https://github.com/BradleyKirton/ice3x
cd ice3x
python -m venv env # virtualenv env
source env/bin/activate
pip install -e .[dev]
pytest
```

# TODO

Note this library is still in beta.

- Write full test suite for sync client
- Write documentation
- Upload to pypi
- Write async client