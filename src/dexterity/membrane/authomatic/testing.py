# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import dexterity.membrane.authomatic


class DexterityMembraneAuthomaticLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=dexterity.membrane.authomatic)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'dexterity.membrane.authomatic:default')


DEXTERITY_MEMBRANE_AUTHOMATIC_FIXTURE = DexterityMembraneAuthomaticLayer()


DEXTERITY_MEMBRANE_AUTHOMATIC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DEXTERITY_MEMBRANE_AUTHOMATIC_FIXTURE,),
    name='DexterityMembraneAuthomaticLayer:IntegrationTesting'
)


DEXTERITY_MEMBRANE_AUTHOMATIC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DEXTERITY_MEMBRANE_AUTHOMATIC_FIXTURE,),
    name='DexterityMembraneAuthomaticLayer:FunctionalTesting'
)


DEXTERITY_MEMBRANE_AUTHOMATIC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DEXTERITY_MEMBRANE_AUTHOMATIC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DexterityMembraneAuthomaticLayer:AcceptanceTesting'
)
