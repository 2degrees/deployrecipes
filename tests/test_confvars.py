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
Test suite for the :class:`ConfvarsRecipe`.

"""
from os import path

from nose.tools import eq_, ok_, assert_raises
from zc.buildout import UserError

from deployrecipes import ConfvarsRecipe


HERE = path.dirname(__file__)

ABS_CONFIG_PATH = path.join(HERE, "fixture", "wsgiapp.ini")
CONFIG_URI = "config:%s" % ABS_CONFIG_PATH

BUILDOUT_DICT = {'buildout': {'directory': path.join(HERE, "fixture")}}


class TestConfvarsRecipe(object):
    """Tests for :class:`ConfvarsRecipe`."""
    
    def test_no_config_uri(self):
        """Parts must define the "config_uri" option."""
        assert_raises(UserError, ConfvarsRecipe, BUILDOUT_DICT, "abc",
                      {'eggs': "foo"})
    
    def test_no_eggs(self):
        """Parts must define the "eggs" option."""
        assert_raises(UserError, ConfvarsRecipe, BUILDOUT_DICT, "abc",
                      {'config_uri': CONFIG_URI})
    
    def test_bad_config_uri(self):
        """Bad "config_uri" values are caught on instantiation."""
        # URI with no scheme:
        assert_raises(UserError, ConfvarsRecipe, BUILDOUT_DICT, "abc",
                      {'config_uri': ABS_CONFIG_PATH, 'eggs': "foo"})
        # URI with scheme, but non-existing path:
        assert_raises(UserError, ConfvarsRecipe, BUILDOUT_DICT, "abc",
                      {'config_uri': "config:%s/nonexisting" % HERE,
                       'eggs': "foo"})
    
    def test_right_config_uri(self):
        """
        The options in the config URI must be loaded into the parts' options.
        
        """
        options = {'config_uri': CONFIG_URI, 'eggs': "foo"}
        ConfvarsRecipe(BUILDOUT_DICT, "abc", options)
        # The new options must have been loaded:
        ok_(len(options) > 1)
        eq_(options['foo'], "bar")
        eq_(options['baz'], "foo")
    
    def test_relative_conf(self):
        """Config URIs are relative to the Buildout directory by default."""
        options = {'config_uri': "config:wsgiapp.ini", 'eggs': "foo"}
        ConfvarsRecipe(BUILDOUT_DICT, "abc", options)
        # The new options must have been loaded:
        ok_(len(options) > 1)
        eq_(options['foo'], "bar")
        eq_(options['baz'], "foo")
    
    def test_installand_update(self):
        """Install and update do nothing."""
        options = {'config_uri': "config:%s" % ABS_CONFIG_PATH, 'eggs': "foo"}
        recipe = ConfvarsRecipe(BUILDOUT_DICT, "abc", options)
        eq_(recipe.install(), None)
        eq_(recipe.update(), None)
