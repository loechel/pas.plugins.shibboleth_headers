from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin


class GroupsPlugin(BasePlugin):
    """ Determine the groups to which a user belongs.
    """
    security = ClassSecurityInfo()

    security.declarePrivate('getGroupsForPrincipal')
    def getGroupsForPrincipal(self, principal, request=None):
        """ principal -> (group_1, ... group_N)

        o Return a sequence of group names to which the principal
          (either a user or another group) belongs.

        o May assign groups based on values in the REQUEST object, if present
        """

        #add your code here

        pass

