from django import forms
from django.templatetags.static import static
from django.utils.safestring import mark_safe
import json
import re


def _sanitize_js_variable_name(s: str):
    """
    Transforms the string to use as variable names in JavaScript.
    """
    # Replace a leading digit with '_'
    s = re.sub(r'^\d', '_', s)
    # Replace any character not allowed in JavaScript variable names with '_'
    s = re.sub(r'[^a-zA-Z0-9_$]', '_', s)
    return s


class TagSelect(forms.widgets.Select):
    class Media:
        js = (static("tagify_widget/vender/tagify/tagify.min.js"),)
        css = {"all": (static("tagify_widget/vender/tagify/tagify.css"),)}

    template_name = "tagify_widget/select.html"

    def __init__(self, attrs=None, choices=()) -> None:
        attrs = {'placeholder': 'Please select'} if attrs is None else attrs
        super().__init__(attrs, choices)
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        data = [
            {
                k: str(o[0][k]) 
                for k in o[0]
                if k in ['value', 'label', 'index']
            } 
            for _, o, _ in context['widget']['optgroups']
        ]

        context["widget"]["tagify"] = {
            "whitelist": mark_safe(json.dumps(data)),
            "varname": _sanitize_js_variable_name(context["widget"]["name"]),
        }
        if isinstance(context["widget"]["value"], list) and len(context["widget"]["value"]):
            context["widget"]["value"] = context["widget"]["value"][0]
        return context


class TagSelectMultiple(TagSelect):
    template_name = "tagify_widget/select_multiple.html"
    option_template_name = "django/forms/widgets/select_option.html"
    allow_multiple_selected = True
