Tests for pas.plugins.shibboleth_headers

test setup
----------

    >>> from Testing.ZopeTestCase import user_password
    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()

Plugin setup
------------

    >>> acl_users_url = "%s/acl_users" % self.portal.absolute_url()
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % ('portal_owner', user_password))
    >>> browser.open("%s/manage_main" % acl_users_url)
    >>> browser.url
    'http://nohost/plone/acl_users/manage_main'
    >>> form = browser.getForm(index=0)
    >>> select = form.getControl(name=':action')

pas.plugins.shibboleth_headers should be in the list of installable plugins:

    >>> 'Shibboleth_Headers Helper' in select.displayOptions
    True

and we can select it:

    >>> select.getControl('Shibboleth_Headers Helper').click()
    >>> select.displayValue
    ['Shibboleth_Headers Helper']
    >>> select.value
    ['manage_addProduct/pas.plugins.shibboleth_headers/manage_add_shibboleth_headers_helper_form']

we add 'Shibboleth_Headers Helper' to acl_users:

    >>> from pas.plugins.shibboleth_headers.plugin import Shibboleth_HeadersHelper
    >>> myhelper = Shibboleth_HeadersHelper('myplugin', 'Shibboleth_Headers Helper')
    >>> self.portal.acl_users['myplugin'] = myhelper

and so on. Continue your tests here

    >>> 'ALL OK'
    'ALL OK'

