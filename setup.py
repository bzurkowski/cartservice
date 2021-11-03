from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name='cartservice',
    version='0.1.0',
    description='Cart Service for Microservices Demo',
    long_description=readme(),
    url='https://github.com/bzurkowski/cartservice',
    author='Bartosz Zurkowski',
    license='Apache License 2.0',
    install_requires=get_requirements(),
    packages=find_packages(),
    zip_safe=False)
