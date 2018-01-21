import re
import os

from setuptools import setup
from setuptools import find_packages

# Some helper functions
def get_version():
  PATTERN = "__version__\s+=\s+'(?P<version>.*)'"

  with open(os.path.join(os.path.dirname(__file__), 'ice3x/__init__.py'), 'r') as f:
      match = re.search(PATTERN, f.read())
      match_dict = match.groupdict()

  return match_dict['version']


def get_readme():
  with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
      readme = f.read()

  return readme


requirements = [
    'requests'
]


if __name__ == '__main__':
    readme = get_readme()
    version = get_version()

    setup(
      name='ice3x',
      version=version,
      author='Bradley Stuart Kirton',
      author_email='bradleykirton@gmail.com',
      packages=find_packages(),
      description='Ice3x Crypto Currency Exchanage Python API',
      url='https://github.com/BradleyKirton/ice3x',
      license='MIT',
      keywords=['exchange', 'crypto currency', 'rest', 'api', 'bitcoin', 'etherium'],
      classifiers=[
         'Development Status :: 4 - Beta',
         'Intended Audience :: Developers',
         'Intended Audience :: Financial and Insurance Industry',
         'Operating System :: OS Independent',
         'Topic :: Office/Business :: Financial :: Investment',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3 :: Only'
      ],
      long_description=readme,
      install_requires=requirements,
      extras_require={'dev': ['pytest', 'requests-mock']}
    )