# -- FILE: example/scoped_hello.py
from __future__ import absolute_import
from jinja2_library import Library
import jinja2.ext

this_library = Library("foo.bar")  # -- HINT: Library with scope="foo.bar".
register = this_library.make_register_decorator()

@register.filter(name="hello")
def hello_filter(value, greeting=None):
    greeting = greeting or "Hello"
    return u"{greeting} {name}".format(greeting=greeting, name=value)

class LibraryExtension(jinja2.ext.Extension):
    def __init__(self, environment):
        super(LibraryExtension, self).__init__(environment)
        this_library.add_to_environment(environment)
