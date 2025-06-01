#!/usr/bin/env python
# -- FILE: example/use_template_library_hello.py
from __future__ import absolute_import, print_function
from jinja2 import Environment
from assertpy import assert_that

this_extension = "example.hello.LibraryExtension"
this_template = "HELLO: {{ this.name|hello(greeting=this.greeting) }}"
this_data = dict(name="Alice", greeting="Ciao")

print("__USE TEMPLATE LIBRARY: {}".format(this_extension))
print("__TEMPLATE:\n{}\n".format(this_template.strip()))

# -- RENDER: this_template
environment = Environment(extensions=[this_extension])
template = environment.from_string(this_template)
this_text = template.render(this=this_data)
print("__RENDERED OUTPUT:\n{}".format(this_text.strip()))
assert_that(this_text).is_equal_to("HELLO: Ciao Alice")
