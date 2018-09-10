from DateTime import DateTime

from Acquisition import aq_inner
from plone import api
from Products.Five import BrowserView
from plone.memoize.view import memoize
from Products.CMFCore.utils import getToolByName
from plone.autoform.form import AutoExtensibleForm
from plone.registry.interfaces import IRegistry
from zope import interface
from zope import schema
from zope.component import getUtility
from z3c.form import form, button, field
from plone.z3cform.layout import wrap_form
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from dexterity.membrane.authomatic import _
from .form import IMemberRegistrationForm

import logging
logger = logging.getLogger(__file__)


class MemberRegistrationForm(AutoExtensibleForm, form.Form):
    schema = IMemberRegistrationForm
    form_name = 'registration_form'

    label = _(u"Registering your profile")
    description = _(u"At the moment, you do not have a profile page. "
                    u"Please fill out the form below to create one.")

    def update(self):
        # disable Plone's editable border
        self.request.set('disable_border', True)


        # call the base class version - this is very important!
        super(MemberRegistrationForm, self).update()
        # user = api.user.get_current()
        # self.fields['email'].field.default = user.getProperty('email')


    @button.buttonAndHandler(_(u'Register'))
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        user = api.user.get_current()
        if not user:
            IStatusMessage(self.request).addStatusMessage(
                    _(u"Please login before continuing"),
                    "error"
                )
            contextURL = "{}/login".format(self.context.absolute_url())
            self.request.response.redirect(contextURL)
            return "redirecting"
        
        email = data.get('email', user.getProperty('email'))
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        name = "{}-{}".format(
            first_name,
            last_name
        )
        success = True
        registry = getUtility(IRegistry)
        membrane_type = registry.get(
            'pas.authomatic.membrane.membrane_type', 'Member'
        )
        with api.env.adopt_roles('Manager'):
            context = api.content.get(path='/profiles')
            base_path = 'profiles/'
            if not context:
                context = self.context
                base_path = ''
            try:
                user = api.content.create(
                    type=membrane_type,
                    container=context,
                    id=name,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=data.get("password"),
                    safe_id=True
                )
            except:
                success = False

        if success:
            IStatusMessage(self.request).addStatusMessage(
                    _(u"Thank you for registering on our platform, please login to complete your profile.",
                    "info")
                )
            portal_url = self.context.absolute_url()
            contextURL = "{0}/{1}{2}/edit".format(
                portal_url,
                base_path,
                user.id
            )
            self.request.response.redirect(contextURL)
        else:
            IStatusMessage(self.request).addStatusMessage(
                    _(u"Something went wrong"),
                    "error"
                )

        
        
        