import re
import os
import shutil
import sys

from setuptools import setup
from setuptools import find_packages

# Some helper functions
def get_version():
  PATTERN = "__version__\s+=\s+'(?P<version>.*)'"

  with open('ice3x/__init__.py', 'r') as f:
      match = re.search(PATTERN, f.read())
      match_dict = match.groupdict()

  return match_dict['version']


def get_readme():
  with open('README.md') as f:
    return f.read()


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('ice3x.egg-info')
    sys.exit()


if __name__ == '__main__':
    version = get_version()
    readme = get_readme()

    setup(
      name='ice3x',
      version=version,
      author='Bradley Stuart Kirton',
      author_email='bradleykirton@gmail.com',
      packages=find_packages(),
      description='Ice3x Crypto Currency Exchanage Python API',
      long_description=readme,
      long_description_content_type='text/markdown',
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
      install_requires=['requests'],
      extras_require={'dev': ['pytest', 'pytest-mock', 'pytest-twisted', 'pypandoc', 'twine'], 'async': ['treq']}
    )