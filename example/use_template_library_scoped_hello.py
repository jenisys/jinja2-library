#!/usr/bin/env python
# -- FILE: example/use_template_library_scoped_hello.py
from __future__ import absolute_import, print_function
from jinja2 import Environment
from assertpy import assert_that

this_extension = "example.scoped_hello.LibraryExtension"
this_template = """HELLO: {{ this.name|foo.bar.hello(greeting="Ciao") }}"""
this_data = dict(name="Bob", greeting="Ciao")

print("__USE TEMPLATE LIBRARY: {}".format(this_extension))
print("__TEMPLATE:\n{}\n".format(this_template.strip()))

# -- RENDER: this_template
environment = Environment(extensions=[this_extension])
template = environment.from_string(this_template)
this_text = template.render(this=this_data)
print("__RENDERED OUTPUT:\n{}".format(this_text.strip()))
assert_that(this_text).is_equal_to("HELLO: Ciao Bob")
