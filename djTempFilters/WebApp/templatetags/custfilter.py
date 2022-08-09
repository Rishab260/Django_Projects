from django import template
register=template.Library()

def trun5(value):
    PyResult=value[0:6]
    return PyResult
register.filter('t5',trun5)