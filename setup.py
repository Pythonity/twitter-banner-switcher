# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

# Convert description from markdown to reStructuredText
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = ''


setup(
    name='twitter-banner-switcher',
    url='https://github.com/Pythonity/twitter-banner-switcher',
    download_url='https://github.com/Pythonity/twitter-banner-switcher/releases/latest',
    bugtrack_url='https://github.com/Pythonity/twitter-banner-switcher/issues',
    version='0.1.0',
    license='MIT License',
    author='Pythonity',
    author_email='pythonity@pythonity.com',
    maintainer='Paweł Adamczak',
    maintainer_email='pawel.adamczak@sidnet.info',
    description="Python script that sets your Twitter profile banner to a "
                "random image from a specified folder or a list of paths.",
    long_description=description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=6.6',
        'PyYAML>=3.11',
        'tweepy>=3.5.0',
    ],
    scripts=['bin/twitter-banner-switcher'],
    keywords='twitter banner',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
)
