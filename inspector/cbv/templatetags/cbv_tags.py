from django import template
from django.conf import settings

register = template.Library()


@register.filter
def called_same(qs, name):
    return [item for item in qs if item.name==name]
