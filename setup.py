from setuptools import setup

setup(
    name='ingredients',
    version='0.0.1',
    author='Jordan Schatz',
    author_email='info@azurestandard.com',
    description='Ingredient Parsing Library',
    license='BSD',
    url='https://github.com/azurestandard/ingredients',
    packages=['ingredients'],
    package_data={'ingredients': ['ingredients-list']},
    long_description='Ingredient Parsing Library'
)