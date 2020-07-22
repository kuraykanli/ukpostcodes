from setuptools import setup

setup(
    name='ukpostcodes',
    packages=['ukpostcodes'],
    version='1.0.0',
    description='Library that validates and formats post codes for UK',
    long_description='This library handles postcode validation and verification over both API requests(remote) and regex(local). The library also includes helper functions for stripping outward and inward codes after validating via regex',
    url='https://github.com/kuraykanli/ukpostcodes',
    author='Kuray Kanli',
    author_email='kuray@kuraykanli.com',
    license='MIT',
    install_requires=['requests']
)
