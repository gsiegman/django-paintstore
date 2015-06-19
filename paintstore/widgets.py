from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            "all": ("%s/%s" % (settings.STATIC_URL, "paintstore/css/colorpicker.css"),)
        }

        js = (
            ("%s/%s" % (settings.STATIC_URL, "paintstore/jquery_1.7.2.js")),
            ("%s/%s" % (settings.STATIC_URL, "paintstore/colorpicker.js")),
            ("%s/%s" % (settings.STATIC_URL, "paintstore/initColorPicker.js")),
        )

    input_type = 'colorpicker'
