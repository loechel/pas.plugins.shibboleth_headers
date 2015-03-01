import install

install.register_shibboleth_headers_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    install.register_shibboleth_headers_plugin_class(context)
