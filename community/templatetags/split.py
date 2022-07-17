from django import template

register = template.Library()

# split 필터
@register.filter(name='split')
def split(value, key):
    return value.split(key)


@register.filter(name='split2')
def split2(value, key):
    result = value.split('//',3)

    result1 = result[1].split(key)
    return result1


@register.filter(name='second')
def second(value):
    """Return the first item in a list."""
    try:
        return value[1]
    except IndexError:
        return ''

@register.filter(name='third')
def third(value):
    """Return the first item in a list."""
    try:
        return value[2]
    except IndexError:
        return 