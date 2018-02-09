#!/usr/bin/env python
from setuptools import setup, find_packages

# versioneer config
import versioneer
versioneer.versionfile_source = 'httpsig_pure_hmac/_version.py'
versioneer.versionfile_build = 'httpsig_pure_hmac/_version.py'
versioneer.tag_prefix = 'v'                 # tags are like v1.2.0
versioneer.parentdir_prefix = 'httpsig-pure-hmac-'    # dirname like 'myproject-1.2.0'

# create long description
with open('README.rst') as file:
    long_description = file.read()
with open('CHANGELOG.rst') as file:
    long_description += '\n\n' + file.read()

setup(
    name='httpsig-pure-hmac',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Fork of httpsig. HMAC only, no RSA, no PyCrypto, pure Python.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='http,authorization,api,web',
    author='Alexander Lukanin',
    author_email='alexander.lukanin.13@gmail.com',
    url='https://github.com/alexanderlukanin13/httpsig-pure-hmac',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['six'],
    test_suite="httpsig_pure_hmac.tests",
)
