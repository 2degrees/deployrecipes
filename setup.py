# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2010, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of deployrecipes:
# <http://bitbucket.org/2degrees/deployrecipes>.
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
version = open(os.path.join(here, "VERSION.txt")).readline().rstrip()

setup(name="deployrecipes",
      version=version,
      description="Buildout recipes for PasteDeploy",
      long_description=README,
      classifiers=[
        "Development Status :: 2 - Pre-Alpha",
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
      author_email="gustavonarea@2degreesnetwork.com",
      url="http://bitbucket.org/2degrees/deployrecipes/",
      license="BSD (http://dev.2degreesnetwork.com/p/2degrees-license.html)",
      packages=find_packages(exclude=["tests"]),
      package_data={
        '': ["VERSION.txt", "README.txt"],
        },
      exclude_package_data={"": ["README.txt"]},
      include_package_data=True,
      zip_safe=False,
      tests_require = [
        "nose >= 0.11.1",
        "coverage",
        ],
      install_requires=[
        "zc.buildout >= 1.4.0",
        "PasteDeploy >= 1.3.3",
        ],
      test_suite="nose.collector",
      entry_points = """\
        [zc.buildout]
        confvars = deployrecipes:ConfvarsRecipe
      """
      )