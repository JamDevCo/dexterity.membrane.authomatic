from plone.login.interfaces import IRedirectAfterLogin
from plone.login.interfaces import IInitialLogin
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.component import getUtility
from zope.interface import implementer
from plone import api

from dexterity.membrane.authomatic import _


@implementer(IRedirectAfterLogin)
class RedirectAfterLoginAdapter(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, came_from=None, is_initial_login=False):
        user = api.user.get_current()
        fullname = safe_unicode(user.getProperty('fullname'))
        
        registry = getUtility(IRegistry)
        membrane_role = registry.get(
            'pas.authomatic.membrane.membrane_role', 'Member'
        )
        welcome_message = registry.get(
            'pas.authomatic.membrane.welcome_message',
            _(u'Thank you for being interested in us. '
              u'Please complete your profile using the link below')
        )
        custom_redirect_path = registry.get(
            'pas.authomatic.membrane.custom_redirect_path', "profile-registration"
        )
        if membrane_role not in api.user.get_roles():
            api.portal.show_message(
                u'Hi {}! {}'.format(
                    fullname,
                    welcome_message
                ),
                self.request
            )
            came_from = "{}/{}".format(
                self.context.portal_url(),
                custom_redirect_path.lstrip("/")
            )
        else:
            api.portal.show_message(
                u'Nice to see you again, {0}!'.format(fullname), self.request)
        if not came_from:
            came_from = self.context.portal_url()
        return came_from