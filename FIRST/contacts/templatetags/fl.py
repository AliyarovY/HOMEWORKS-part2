from django import template


register = template.Library()


@register.simple_tag
def mediapath(x):
    return f'/media/{x}'
