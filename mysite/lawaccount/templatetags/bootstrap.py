from django.template import Context
from django.template.loader import get_template
from django import template
import sys

register = template.Library()

TEMPLATE_PATH = 'lawaccount/'

@register.filter
def bootstrap(element, template_name='form.html'):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    print >>sys.stderr, 'doing bootstrap:' + template_name
    return render(element, markup_classes, template_name)

def bootstrap_default(element, template_name='form.html'):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    print >>sys.stderr, 'doing bootstrap:' + template_name
    return render(element, markup_classes, template_name)


@register.filter
def bs3field(element):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    return render2(element, markup_classes, 'form_field.html')

@register.filter
def bootstrap_inline(element, template_name='form.html'):
    markup_classes = {'label': 'sr-only', 'value': '', 'single_value': ''}
    return render(element, markup_classes,template_name)


@register.filter
def bootstrap_horizontal(element, label_cols={},template_name='form.html'):
    if not label_cols:
        label_cols = 'col-sm-2 col-lg-2'

    markup_classes = {'label': label_cols,
            'value': '',
            'single_value': ''}

    for cl in label_cols.split(' '):
        splited_class = cl.split('-')

        try:
            value_nb_cols = int(splited_class[-1])
        except ValueError:
            value_nb_cols = 12

        if value_nb_cols >= 12:
            splited_class[-1] = 12
        else:
            offset_class = cl.split('-')
            offset_class[-1] = 'offset-' + str(value_nb_cols)
            splited_class[-1] = str(12 - value_nb_cols)
            markup_classes['single_value'] += ' ' + '-'.join(offset_class)
            markup_classes['single_value'] += ' ' + '-'.join(splited_class)

        markup_classes['value'] += ' ' + '-'.join(splited_class)

    return render(element, markup_classes,template_name)


def add_input_classes(field):
    if not is_checkbox(field) and not is_multiple_checkbox(field) and not is_radio(field):
        field_classes = field.field.widget.attrs.get('class', '')
        if not ('form-control' in field_classes):
            field_classes += ' form-control'
            field.field.widget.attrs['class'] = field_classes


def render2(element,markup_classes, template_name):
    add_input_classes(element)
    template = get_template(TEMPLATE_PATH + template_name)
    if not element.label.strip():
        print >>sys.stderr, 'No Label'
        markup_classes['label']='sr-only'

    context = Context({'field': element, 'classes': markup_classes})
    return template.render(context)

def render(element, markup_classes, template_name):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template(TEMPLATE_PATH + template_name)
        context = Context({'field': element, 'classes': markup_classes})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template(TEMPLATE_PATH + "formset.html")
            context = Context({'formset': element, 'classes': markup_classes})
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template(TEMPLATE_PATH + template_name)
            context = Context({'form': element, 'classes': markup_classes})

    return template.render(context)


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_multiple_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxselectmultiple"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"
