
from django import template

register = template.Library()

@register.filter(name ='cuttin')
def cuttin(value, arg):
    """ This cuts out all values of arg from the string
    """
    return value.replace(arg,"")

#register.filter('cuttin',cuttin)

