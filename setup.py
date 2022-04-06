# get version from __version__ variable in library_management/__init__.py
from library_management import __version__ as version

setup(
	name="library_management",
	version=version,
	description="This app is a custom app built for library management system",
	author="Bakr Aldubai",
	author_email="eng.bakraldubai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)