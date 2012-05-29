import os
import codecs
import re
from setuptools import setup


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-paintstore',
    version=find_version("paintstore", "__init__.py"),
    description='A Django app that integrates jQuery ColorPicker with the Django admin.',
    long_description=read('README.rst'),
    author='Glenn Siegman',
    author_email='gsiegman@gsiegman.com',
    license='MIT',
    url='https://github.com/gsiegman/django-paintstore',
    packages=['paintstore',],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)