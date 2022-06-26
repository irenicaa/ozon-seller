import os.path
import sys

import setuptools

PYTHON_VERSION = '>=3.9.13, <4.0.0'
if not (0x03090df0 <= sys.hexversion < 0x040000f0):
    raise Exception('requires Python ' + PYTHON_VERSION)

packages = setuptools.find_packages()
package_name = packages[0]
project_name = package_name.replace('_', '-')

project_path = os.path.dirname(os.path.abspath(__file__))

setuptools.setup(
    name=project_name,
    version='1.0.0',
    description='Ozon seller library',
    license='MIT',
    author='irenica',
    author_email='root@irenica.pro',
    url='https://github.com/irenicaa/' + project_name,
    packages=packages,
    install_requires=[
        'dataclasses_json >=0.5.7, <1.0.0',
        'marshmallow >=3.16.0, <4.0.0',
        'requests >=2.28.0, <3.0.0',
    ],
    python_requires=PYTHON_VERSION,
)
