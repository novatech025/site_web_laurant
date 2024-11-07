from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime
from django.utils import timezone
# from dateutil.parser import parse
# from dateutil.utils

register = template.Library()



@register.filter("filter_selected")
@stringfilter
def filter_selected(value, selected_type):
    return selected_type if selected_type != value else "uk-active"

