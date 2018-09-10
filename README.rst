.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
dexterity.membrane.authomatic
==============================================================================

This is a Plone add-on that is use to make users as content for acl_users or users
that does not have a membrane user profile especially for users that were created
using [pas.plugins.authomatic](https://github.com/collective/pas.plugins.authomatic) package.

Features
--------

- Turns existing users to content.
- Offers a custom handler for converting users to content.

![PAS Authomatic Membrane Settings](https://image.ibb.co/dPTyZp/PAS_Authomatic_Membrane_Settings.png)

Upon on logging in without the Role seen in the screenshot above, the user will be
redirected to the profile registration page.

![Profile Registration](https://image.ibb.co/jRMwLU/Profile_Registration.png)


Installation
------------

Install dexterity.membrane.authomatic by adding it to your buildout::

    [buildout]

    ...

    eggs =
        dexterity.membrane.authomatic


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/dexterity.membrane.authomatic/issues
- Source Code: https://github.com/collective/dexterity.membrane.authomatic


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: b4.oshany@gmail.com


License
-------

The project is licensed under the GPLv2.
