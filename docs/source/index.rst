Buildout recipes for PasteDeploy
================================

:Sponsored by: `2degrees Limited <http://dev.2degreesnetwork.com/>`_.
:Latest release: |release|

.. topic:: Overview

    **DeployRecipes** implements some `Buildout <http://www.buildout.org/>`_
    recipes for `PasteDeploy <http://pythonpaste.org/deploy/>`_.

The recipes
===========

*confvars*: Load options from PasteDeploy configuration files
-------------------------------------------------------------

The *confvars* recipe loads the options from a PasteDeploy configuration file
into a Buildout part, so you can define variables in a single place and use them
within your Buildout configuration.

The URI given must be absolute or relative to the Buildout directory.

Example
~~~~~~~

Say you have the following PasteDeploy config:

.. code-block:: ini

    # /path/to/config.ini
    [DEFAULT]
    debug = false
    
    [app:main]
    use = egg:yourpackage
    database_name = db1
    database_password = passw0rd


You may want to reuse the ``database_name`` and ``database_password`` options
in a recipe that sets the database up. In that case, you would use a Buildout
configuration file like the one below:

.. code-block:: ini

    [buildout]
    parts = setup_db
    
    [paste_vars]
    recipe = deployrecipes:confvars
    config_uri = config:/path/to/config.ini
    factory_distribution = yourpackage
    
    [setup_db]
    recipe = your_recipe_to_setup_the_database
    database_name = ${paste_vars:database_name}
    database_password = ${paste_vars:database_password}

Or just:

.. code-block:: ini

    [buildout]
    parts = setup_db
    
    [paste_vars]
    recipe = deployrecipes:confvars
    config_uri = config:/path/to/config.ini
    factory_distribution = yourpackage
    
    [setup_db]
    <= paste_vars
    recipe = your_recipe_to_setup_the_database


This recipe internally uses `zc.recipe.egg <http://pypi.python.org/pypi/zc.recipe.egg>`_,
so you could use any of its options if you need it.


.. attention::

    It's mandatory to set the ``factory_distribution`` option to the package
    that provides the PasteDeploy application factory! Otherwise you will get
    import errors (``DistributionNotFound``).


Links
=====

- `Online documentation <http://packages.python.org/deployrecipes/>`_.
- `Support mailing list <http://groups.google.com/group/2degrees-floss/>`_.
- `Ohloh entry <https://www.ohloh.net/p/deployrecipes>`_ -- Vote for it if you
  use it and find it useful!
- `Development Web site <https://github.com/2degrees/deployrecipes/>`_:
  The place to report bugs, request features and get the source code.


More information
================

.. toctree::
   :maxdepth: 2
   
   changelog
