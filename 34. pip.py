"""
PIP(Preferred Installation Program), is a package manager for python packages.
A package contains all the files you need for a module.
Modules are python code libraries you can include in your project.

Check if PIP is Installed.
...\Python\Python36-32\Scripts>pip --version
Otherwise download link is:  https://pypi.org/project/pip/
Download a package: ....\Scripts>pip install camelcase
Uninstall command to remove a package: pip uninstall camelcase.
List command to list all the packages installed: pip list.
"""
import CamelCase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
