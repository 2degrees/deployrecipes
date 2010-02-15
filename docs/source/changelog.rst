**PasteDeploy** releases
========================

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
