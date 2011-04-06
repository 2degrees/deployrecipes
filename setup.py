# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2010-2011, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of deployrecipes:
# <http://packages.python.org/deployrecipes/>.
#
# deployrecipes is subject to the provisions of the BSD license that accompanies
# that distribution. An incomplete copy of that text is also available at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. THIS SOFTWARE IS
# PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE,
# MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
################################################################################
import os

# Setuptools is obviously available, so there's no need to use ez_setup:
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGELOG = open(os.path.join(here, "docs", "source", "changelog.rst")).read()
version = open(os.path.join(here, "VERSION.txt")).readline().rstrip()

setup(name="deployrecipes",
      version=version,
      description="Buildout recipes for PasteDeploy",
      long_description="\n".join((README, CHANGELOG)),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Buildout",
        "Framework :: Paste",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        ],
      keywords="buildout recipe wsgi paste deploy web PasteDeploy",
      author="2degrees Limited",
      author_email="2degrees-floss@googlegroups.com",
      url="http://packages.python.org/deployrecipes/",
      license="BSD (http://dev.2degreesnetwork.com/p/2degrees-license.html)",
      py_modules=["deployrecipes"],
      package_data={
        '': ["VERSION.txt", "README.txt"],
        'docs': ["Makefile", "source/*"],
        },
      include_package_data=True,
      tests_require = [
        "nose >= 0.11.1",
        "coverage",
        ],
      install_requires=[
        "zc.buildout >= 1.4.0",
        "zc.recipe.egg >= 1.2.2",
        "PasteDeploy >= 1.3.3",
        "Paste",
        ],
      test_suite="nose.collector",
      entry_points = """\
        [zc.buildout]
        confvars = deployrecipes:ConfvarsRecipe
      """
      )
