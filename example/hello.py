# -- FILE: example/hello.py
from jinja2_library import Library
import jinja2.ext

this_library = Library()
register = this_library.make_register_decorator()

@register.filter
def hello(value, greeting=None):
    greeting = greeting or "Hello"
    return u"{greeting} {name}".format(greeting=greeting, name=value)

class LibraryExtension(jinja2.ext.Extension):
    """Simplifies to use ``this_library`` as Jinja2 extension."""
    def __init__(self, environment):
        super(LibraryExtension, self).__init__(environment)
        this_library.add_to_environment(environment)
