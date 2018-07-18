"""
Wed Jul 18 05:40:41 IST 2018
source :-https://www.geeksforgeeks.org/template-class-in-python/
Template Class allows us to create simplified syntax for output specification.
The format uses placeholder names formed by $ with valid Python identifiers
in StringTemplate we will create a generalised output specification then we will use that at requred generalised form

"""
from string import Template

names_list = ['Sai kumar', 'Nagesh', 'Durga', 'RGV']
# creating a template with placeholder

t = Template('Hi Mr.$name ')  # $name is a placeholder
for i in names_list:
    print(t.substitute(name=i))


