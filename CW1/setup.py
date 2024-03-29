from setuptools import setup, find_packages

setup(
    name="alchemist",
    version="1.0.0",
    author = "Joseph Weston",
    packages=find_packages(exclude=['*tests']),
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts':[
            'abracadabra = alchemist.command:abracadabra'
        ]})