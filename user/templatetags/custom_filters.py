# templatetags/custom_filters.py
from django import template
import validators

register = template.Library()

@register.filter(name='is_valid_url')
def is_valid_url(value):
    return validators.url(value) if value else False
