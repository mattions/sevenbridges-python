import io
import os
import re
import sys
from setuptools import setup, find_packages


# If version file exists, this happens during the installation phase,
# read the version from the version file.
# If the version file does not exist, this is during the build phase,
# read the version from TRAVIS_TAG and create a version file for packaging.
VERSION_FILE = 'VERSION'
if os.path.isfile(VERSION_FILE):
    with io.open(VERSION_FILE, 'r', encoding='utf-8') as f:
        version = f.read()
else:
    version = os.environ.get('TRAVIS_TAG', '0.0.0')
    with io.open(VERSION_FILE, 'w', encoding='utf-8') as f:
        f.write(version)


with open('requirements.txt') as fp:
    install_requires = fp.readlines()
if sys.version_info < (3, 0):
    reg = re.compile('''^.*?;\s*python_version\s*<\s*'3\..*$''')
    install_requires = [i for i in install_requires if not reg.match(i)]


setup(
    name='sevenbridges-python',
    version=version,
    description='SBG API python client bindings',
    install_requires=install_requires,
    long_description=io.open('README.rst', 'r').read(),
    platforms=['Windows', 'POSIX', 'MacOS'],
    maintainer='Seven Bridges Genomics Inc.',
    maintainer_email='senad.ibraimoski@sbgenomics.com',
    url='https://github.com/sbg/sevenbridges-python',
    license='Apache Software License 2.0',
    include_package_data=True,
    packages=find_packages(exclude=["*.tests"]),
    keywords=['sevenbridges', 'sbg', 'api', 'cgc', 'cancer', 'genomics',
              'cloud'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
