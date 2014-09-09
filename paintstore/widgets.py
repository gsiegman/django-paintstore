from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            "all": ("%s/%s" % (settings.STATIC_URL, "paintstore/css/colorpicker.css"),)
        }

        js  = (
            ("%s/%s" % (settings.STATIC_URL, "paintstore/jquery_1.7.2.js")),
            ("%s/%s" % (settings.STATIC_URL, "paintstore/colorpicker.js"))
        )

    input_type = 'colorpicker'

    def render(self, name, value, attrs=None):
        script = u"""<script type='text/javascript'>
                        $(document).ready(function(){{
                            $('#{0}').ColorPicker({{
                                onSubmit: function(hsb, hex, rgb, el, parent) {{
                                    $(el).val('#' + hex);
                                    $(el).ColorPickerHide();
                                    $('#{0}').css('background-color', '#' + hex);
                                }},
                                onBeforeShow: function () {{
                                    $(this).ColorPickerSetColor(this.value);
                                }}
                            }}).bind('keyup', function(){{
                                $(this).ColorPickerSetColor(this.value.replace('#', ''));
                            }});
                            $('#{0}').css('background-color', $('#{0}').val());
                        }});
                    </script>
                    """.format(u'id_'+name)

        super_render = super(ColorPickerWidget, self).render(name, value, attrs)
        return mark_safe(u"%s%s" % (super_render, script))
