from django import template

register = template.Library()

# Register using filter decorator
@register.filter(name='cut')
def cut(value, arg):
    arg = arg.lower()
    return value.replace(arg, '')


# register.filter('cut', cut)
