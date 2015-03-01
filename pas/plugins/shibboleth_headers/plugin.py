"""Class: Shibboleth_HeadersHelper
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

import interface
import plugins

class Shibboleth_HeadersHelper( # -*- implemented plugins -*-
                    plugins.groups.GroupsPlugin,
                    plugins.group_enumeration.GroupEnumerationPlugin,
                               ):
    """Multi-plugin

    """

    meta_type = 'shibboleth_headers Helper'
    security = ClassSecurityInfo()

    def __init__( self, id, title=None ):
        self._setId( id )
        self.title = title



classImplements(Shibboleth_HeadersHelper, interface.IShibboleth_HeadersHelper)

InitializeClass( Shibboleth_HeadersHelper )
