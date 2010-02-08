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
"""
Buildout recipes for PasteDeploy.

"""
from zc.buildout import UserError as BuildoutError
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
        if "eggs" not in options:
            raise BuildoutError('"eggs" option not set in [%s] to the package '
                                'containing the PasteDeploy application '
                                'factory' % name)
        
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

