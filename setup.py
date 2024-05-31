#!/usr/bin/env python
import codecs
import os
import re
import sys

if os.name == "nt" and ("build" in sys.argv or "bdist_msi" in sys.argv):
    from cx_Freeze import Executable, setup
    from setuptools import find_packages

    build_exe_options = {
        "includes": ["awscli", "html.parser"],
        "packages": ["docutils"],
        "excludes": ["awscli.examples", "botocore.data"],
    }
    build_msi_options = {
        "add_to_path": True,
        "skip_build": True,
        "upgrade_code": "{799865ae-6f18-4e1a-a396-2ee83b6b46a8}",
    }
    cx_freeze_opts = {
        "options": {"build_exe": build_exe_options, "bdist_msi": build_msi_options},
        "executables": [Executable("bin/nifcloud", icon="assets/icon.ico")],
    }
else:
    from setuptools import find_packages, setup
    cx_freeze_opts = {}


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as f:
        content = f.read()
    return content


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]',
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='nifcloud-cli',
    version=find_version('nifcloudcli', '__init__.py'),
    description='NIFCLOUD Command-Line Tools',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Fujitsu',
    url='https://github.com/nifcloud/nifcloud-cli',
    packages=find_packages(exclude=['tests*']),
    package_data={'nifcloudcli': ['data/*.json', 'topics/*.json']},
    include_package_data=True,
    install_requires=['nifcloud==1.13.0', 'awscli==1.29.1', 'pyyaml==5.3.1'],
    license='Apache License 2.0',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ),
    scripts=['bin/nifcloud'],
    **cx_freeze_opts,
)
