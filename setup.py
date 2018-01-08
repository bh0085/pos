from setuptools import setup

setup(
    name='AERONAUT pos',
    version='.1',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'pyquery', 'requests' ]
)
