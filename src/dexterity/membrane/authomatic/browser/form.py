from plone.autoform.form import AutoExtensibleForm
from zope import interface
from zope import schema
from plone import api
from plone.supermodel import model
from plone.autoform import directives
from collective import dexteritytextindexer
from plone.app.z3cform.widget import AjaxSelectFieldWidget, SelectFieldWidget
from zope import component
from z3c.form import form, button
from dexterity.membrane.content.member import IEmail
from plone.schema.email import Email
from zope.interface import Invalid
from zope.interface import invariant

from Products.statusmessages.interfaces import IStatusMessage
from dexterity.membrane.authomatic import _


class  IMemberRegistrationForm(IEmail):
    first_name = schema.TextLine(
        title=_(u"First Name")
    )
    last_name = schema.TextLine(
        title=_(u"Last Name"),
    )
    password = schema.Password(
        title=_(u'Password')
    )
    confirm_password = schema.Password(
        title=_(u'Confirm Password')
    )
    
    @invariant
    def password_invariant(data):
        if data.confirm_password != data.password:
            raise Invalid(_(u'Password fields do not match'))


class MemberRegistrationAdapter(object):
    interface.implements(IMemberRegistrationForm)
    component.adapts(interface.Interface)

    def __init__(self, context):
        self.password = None
        self.confirm_password = None
        self.email = None
        user = api.user.get_current()
        self.email = user.getProperty('email')
        
        fullname = user.getProperty('fullname')
        if not fullname:
            self.first_name = None
            self.last_name = None
        else:
            fullname = fullname.split(' ')
            self.first_name = fullname[0]
            self.last_name = fullname[-1]


