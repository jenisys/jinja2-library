#!/usr/bin/env python
# -- FILE: example/use_template_library_hello2.py
from __future__ import absolute_import, print_function
from jinja2 import Environment
from assertpy import assert_that

this_extension = "example.hello2.LibraryExtension"
this_template = """
HELLO_1: {{this.name|hello}}
HELLO_2: {{this.name|hello(greeting="Ciao")}}
"""
this_data = dict(name="Charly")

print("__USE TEMPLATE LIBRARY: {}".format(this_extension))
print("__TEMPLATE:\n{}\n".format(this_template.strip()))

# -- RENDER: this_template
environment = Environment(extensions=[this_extension])
template = environment.from_string(this_template)
this_text = template.render(this=this_data)
print("__RENDERED OUTPUT:\n{}".format(this_text.strip()))
assert_that(this_text).contains("HELLO_1: Hello Charly")
assert_that(this_text).contains("HELLO_2: Ciao Charly")
