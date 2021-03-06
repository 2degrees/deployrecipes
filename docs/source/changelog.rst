**DeployRecipes** releases
==========================

Version 1.0.1 (unreleased)
--------------------------

- Included changelog file in distribution because it's needed by ``setup.py``.
  The previous approach stopped working in newer versions of setuptools.


Version 1.0 Final (2013-09-24)
------------------------------

Minor internal changes made:

- Converted :meth:`ConfvarsRecipe.get_config_variables` to a protected method.
- Exposed static method
  :meth:`ConfvarsRecipe.get_config_variables_from_app_config` to allow for
  sub-classing.


Version 1.0 Release Candidate 2 (2013-06-19)
--------------------------------------------

- Made ``install`` method on recipe return an empty tuple to tell Buildout that
  no file was updated.
- Exposed method ``get_config_variables`` on recipe to allow for sub-classing.
- Excluded options in ``global_conf`` from the options made available to other
  recipes.


Version 1.0 Release Candidate 1 (2011-04-06)
--------------------------------------------

- Updated minimum version of ``zc.recipe.egg`` to 1.2.2.


Version 1.0 Alpha 5 (2010-02-15)
--------------------------------

- Lowered the required version of *zc.recipe.egg* to v1.1.


Version 1.0 Alpha 4 (2010-02-15)
--------------------------------

- Renamed the ``eggs`` option to ``factory_distribution`` in the ``confvars``
  recipe.
- Made the ``confvars`` recipe really load the distribution that provides the
  PasteDeploy application factory. Thanks to Jim Fulton for explaining how to
  do it!


Version 1.0 Alpha 3 (2010-02-10)
--------------------------------

- Fixed packaging problem, where the module was not included in the distribution.


Version 1.0 Alpha 2 (2010-02-10)
--------------------------------

- Fixed typos in the documentation.
- Added `Paste itself <http://pythonpaste.org/>`_ as a dependency, to avoid
  import errors.


Version 1.0 Alpha 1 (2010-02-08)
--------------------------------

Implemented the **confvars** recipe.
