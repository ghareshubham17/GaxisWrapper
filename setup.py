from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gaxiswrapper/__init__.py
from gaxiswrapper import __version__ as version

setup(
	name="gaxiswrapper",
	version=version,
	description="gaxis",
	author="shubham",
	author_email="ghareshubham88@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
