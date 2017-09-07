from setuptools import setup, find_packages

packages = find_packages(include=['cryptocompare'])

setup(
    name='cryptocompare',
    version='0.1',
    description="Python access to crymptcompare api",
    packages=packages,
    install_requires=[
        'requests>=2.1'
    ]
)
