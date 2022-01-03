from django import template

register = template.Library()

#DECORATORS
@register.filter(name='cut')   # cut = new register(cut)
def cut(value,arg):
    """
    This cut out all value of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
