# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from plone import api
from Products.CMFPlone.interfaces import constrains


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'dexterity.membrane.authomatic:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    setup_users_profile_dir_setup(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def setup_users_profile_dir_setup(context, portal=None):
    if not portal:
        portal = api.portal.get()

    #check for the existence of meetings and documents
    #
    profiles_dir = api.content.get('/profiles')
    if not profiles_dir:
        profiles_dir = api.content.create(
            portal,
            'Folder',
            id='profiles',
            title='Profiles',
            description='List of user profiles'
        )
        api.content.transition(profiles_dir, transition='publish')
