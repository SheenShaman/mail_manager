from django import template

register = template.Library()


@register.simple_tag
def mymedia(val):
    return f'/media/{val}'
