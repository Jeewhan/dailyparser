# -*- coding: utf-8 -*-
from setuptools import setup


try:
    with open('README.md') as f:
        readme = f.read()
    with open('requirements.txt') as f:
        requirements = f.readlines()

except IOError:
   readme = ''
   requirements = ''


setup(
   name="CheckBalance",
   version='0.1.0',
   py_modules=['flask_boto_sqs'],
   author='Beomi',
   author_email='jun at beomi dot net',
   url='https://github.com/Beomi/KoreaBankChecker',
   description="Python Module for Korea Bank Checking",
   long_description=readme,
   install_requires=requirements,
)