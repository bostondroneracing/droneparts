from setuptools import setup, find_packages

setup(
    name='droneparts',
    description="Parts library for developing drones",
    version='0.2dev',
    packages=find_packages(),
    install_requires=['solidpython'],
    include_package_data = True,
    author="Wil Koch",
    license='Creative Commons Attribution-Noncommercial-Share Alike license'
)
