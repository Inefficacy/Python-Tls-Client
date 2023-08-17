#!/usr/bin/env python
from setuptools import setup, find_packages, Extension
from codecs import open
from glob import glob
from os import path
from json import loads
from urllib3 import PoolManager

http = PoolManager()
r = http.request('GET', 'https://api.github.com/repos/bogdanfinn/tls-client/releases/latest')
if r.status != 200:
    print('Failed to download tls-client library manually, download from https://github.com/bogdanfinn/tls-client/releases/latest')
else:
    for asset in loads(r.data.decode('utf-8'))['assets']:
        name = asset['name']
        if name.endswith('.h') or 'xgo' in name:
            continue
        name = '.'.join(['-'.join(name.split('-')[:-1]), name.split('.')[-1]])
        with open(path.join(path.dirname(__file__), 'tls_client', 'dependencies', name), 'wb') as f:
            r = http.request('GET', asset['browser_download_url'])
            f.write(r.data)
    print('Downloaded libraries')

data_files = []
directories = glob('tls_client/dependencies/')
for directory in directories:
    files = glob(directory+'*')
    data_files.append(('tls_client/dependencies', files))

about = {}
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "tls_client", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    description=about["__description__"],
    license=about["__license__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*'],
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ]
)