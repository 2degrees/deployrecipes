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
"""
Buildout recipes for PasteDeploy.

"""
from zc.buildout import UserError as BuildoutError
from zc.recipe.egg import Eggs
from pkg_resources import working_set

from paste.deploy.loadwsgi import appconfig


class ConfvarsRecipe(object):
    """
    Recipe to load the options from a PasteDeploy config URI into the Buildout
    parts.
    
    """
    
    def __init__(self, buildout, name, options):
        if "config_uri" not in options:
            raise BuildoutError('PasteDeploy config URI not set in the '
                                '"config_uri" option')
        
        # Loading the distribution:
        distribution = options.pop("factory_distribution", None)
        if not distribution:
            raise BuildoutError('"factory_distribution" option not set in [%s] '
                                'to the package containing the PasteDeploy '
                                'application factory' % name)
        if "eggs" not in options:
            # If we don't set the "eggs" option, it will take the part name:
            options['eggs'] = ""
        ws = Eggs(buildout, name, options).working_set([distribution])[1]
        for dist in ws:
            working_set.add(dist)
        
        # Loading the variables in the PasteDeploy config:
        buildout_dir = buildout['buildout']['directory']
        try:
            config_variables = appconfig(options['config_uri'], 
                                         relative_to=buildout_dir)
        except (LookupError, ValueError, OSError), exc:
            raise BuildoutError("Could not load variables from part '%s': %s"
                                % (name, exc))
        else:
            options.update(config_variables)
    
    def install(self):
        pass
    
    def update(self):
        pass

