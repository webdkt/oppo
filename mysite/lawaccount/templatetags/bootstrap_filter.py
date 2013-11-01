from django import template

register = template.Library()

@register.filter(name='bs3style')
def bs3_css(field):
    """add bootstrap 3.0 css"""
	output_html = '<div class="form-group">
						<label class="col-
    return "It just works!!! " #field.as_widget(attrs={"class":'form-control'})