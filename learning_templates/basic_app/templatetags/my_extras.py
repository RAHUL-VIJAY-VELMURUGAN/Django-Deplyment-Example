from django import template

register = template.Library()

def cuts(value,arg):
    """
    This cut out all value of args
    """
    return value.replace(arg,'')

register.filter('cuts',cuts)
