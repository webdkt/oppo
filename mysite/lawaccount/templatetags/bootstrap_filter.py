from django import template

register = template.Library()

@register.filter(name='bs3style')
def bs3_css(field):
    """add bootstrap 3.0 css"""
    return "It just works!!! " #field.as_widget(attrs={"class":'form-control'})