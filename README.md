# ICE3X Python Library

This ice3x library is a Python package compliant with the ICE3X APi version 2.

This package is essentially a port of the official [PHP client](https://github.com/ICE3X/v2-PHP).

Note this library is still in beta.

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