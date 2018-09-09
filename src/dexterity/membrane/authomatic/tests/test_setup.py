# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from dexterity.membrane.authomatic.testing import DEXTERITY_MEMBRANE_AUTHOMATIC_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that dexterity.membrane.authomatic is properly installed."""

    layer = DEXTERITY_MEMBRANE_AUTHOMATIC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dexterity.membrane.authomatic is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'dexterity.membrane.authomatic'))

    def test_browserlayer(self):
        """Test that IDexterityMembraneAuthomaticLayer is registered."""
        from dexterity.membrane.authomatic.interfaces import (
            IDexterityMembraneAuthomaticLayer)
        from plone.browserlayer import utils
        self.assertIn(IDexterityMembraneAuthomaticLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DEXTERITY_MEMBRANE_AUTHOMATIC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['dexterity.membrane.authomatic'])

    def test_product_uninstalled(self):
        """Test if dexterity.membrane.authomatic is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'dexterity.membrane.authomatic'))

    def test_browserlayer_removed(self):
        """Test that IDexterityMembraneAuthomaticLayer is removed."""
        from dexterity.membrane.authomatic.interfaces import IDexterityMembraneAuthomaticLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDexterityMembraneAuthomaticLayer, utils.registered_layers())
