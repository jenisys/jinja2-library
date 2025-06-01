# -*- coding: UTF-8 -*-
"""
Provides the complete example for a template library (that is used in tests).
"""

from __future__ import absolute_import, print_function
from jinja2_library import Library
import jinja2.ext


# -----------------------------------------------------------------------------
# TEMPLATE LIBRARY:
# -----------------------------------------------------------------------------
this_library = Library()
register = this_library.make_register_decorator()


@register.filter(name="hello")
def hello_filter(value, greeting=None):
    """EXAMPLE:

    .. code-block:: jinja

        {{ "Alice"|hello }}
        {{ "Alice"|hello() }}
        {{ "Alice"|hello(greeting="Ciao") }}
    """
    greeting = greeting or "Hello"
    return u"{greeting} {name}".format(greeting=greeting, name=value)


@register.global_(name="hello")
def hello_global(value, greeting=None):
    """EXAMPLE:

    .. code-block:: jinja

        {{ hello("Bob") }}
        {{ hello("Bob", greeting="Bonjour") }}
    """
    greeting = greeting or "Hello"
    return u"{greeting} {name}".format(greeting=greeting, name=value)


@register.extension
class HelloTagExtension(jinja2.ext.Extension):
    """Simple Jinja2 extension example.

    EXAMPLE:

    .. code-block:: jinja

        {% hello -%} world {%- endhello %}

    .. code-block:: txt

        HELLO world
    """
    tags = set(["hello"])

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(["name:endhello"],
                                       drop_needle=True)
        return jinja2.nodes.CallBlock(
            self.call_method("_hello"), [], [], body).set_lineno(lineno)
        # -- RETURN: nodes.CallBlock/Call that is executed later-on.

    def _hello(self, caller):
        captured_text = caller()
        return "HELLO {0}".format(captured_text)


# -----------------------------------------------------------------------------
# JINJA LIBRARY EXTENSION: For this_library
# -----------------------------------------------------------------------------
class LibraryExtension(jinja2.ext.Extension):
    """Simplify use of ``this_library`` in :class:`jinja2.Environment`."""
    def __init__(self, environment):
        super(LibraryExtension, self).__init__(environment)
        this_library.add_to_environment(environment)
