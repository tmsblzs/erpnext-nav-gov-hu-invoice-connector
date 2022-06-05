from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nav_gov_hu_invoice_connector/__init__.py
from nav_gov_hu_invoice_connector import __version__ as version

setup(
	name="nav_gov_hu_invoice_connector",
	version=version,
	description="It is connecto to online invoice system of hungarion tax authority.",
	author="tmsblzs",
	author_email="tmsblzs+github@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
