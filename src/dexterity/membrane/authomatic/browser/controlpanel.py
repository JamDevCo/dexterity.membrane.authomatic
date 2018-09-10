from zope.interface import Interface
from zope import schema
from Products.CMFCore.interfaces import ISiteRoot
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from plone.z3cform import layout
from plone.directives import form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from jamaicandevelopers.site import _


class IProfileRegistration(form.Schema):
    membrane_role = schema.Choice(
        title=_(u'Role for dexterity.membrane Member'),
        description=_(
            u'help_memberance',
            default=_(
                u'Select the role, which a user must have to create '
                u'a profile on your site. Whenever a user logs in, who does '
                u'not have the selected role, they will be redirected to '
                u'${navigational_url}/profile-registration')
        ),
        required=False,
        default=u'Member',
        missing_value=u'',
        vocabulary='plone.app.vocabularies.Roles'
    )
    membrane_type = schema.Choice(
        title=_(u'Select the content type, which your '
                u'dexterity.membrane.Member objects are using '),
        required=False,
        missing_value=u'',
        vocabulary='plone.app.vocabularies.PortalTypes'
    )
    
    welcome_message = schema.Text(
        title=_(u'Welcome message after successfully logging in.'),
        description=_(
            u'help_welcome_message',
            default=_(
                u'The welcome message will display below the base message, '
                u'Hi <user fullname>')
        ),
        required=False,
        missing_value=u'',
    )
    
    custom_redirect_path = schema.TextLine(
        title=_(u'Redirect non-membrane users to the path given.'),
        description=_(
            u'help_custom_redirect_path',
            default=_(
                u'If left empty, the default profile registration will be used'
            )
        ),
        required=False,
        missing_value=u'',
    )


class ProfileRegistrationForm(RegistryEditForm):
    """
    Content Categories
    """
    schema = IProfileRegistration
    schema_prefix = "pas.authomatic.membrane"
    label = (u"Profile Registration Form")

    def getContent(self):
        try:
            data = super(ProfileRegistrationForm, self).getContent()
        except KeyError:
            data =  {
                'membrane_role': u'Member',
                'welcome_message': u'',
                'custom_redirect_path': u'',
                'membrane_type': u''
            }
            registry = getUtility(IRegistry)
            registry.registerInterface(IProfileRegistration)
        return data


ProfileRegistrationFormView = layout.wrap_form(
   ProfileRegistrationForm, ControlPanelFormWrapper)


