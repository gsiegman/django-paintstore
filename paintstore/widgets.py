from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage


class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            "all": (staticfiles_storage.url("paintstore/css/colorpicker.css"),),
        }

        js = (
            staticfiles_storage.url("paintstore/jquery_1.7.2.js"),
            staticfiles_storage.url("paintstore/colorpicker.js")
        )

    input_type = 'colorpicker'

    def render(self, name, value, attrs=None):
        script = u"""<script type='text/javascript'>
                        $(document).ready(function(){
                            $('#%s').ColorPicker({
                                onSubmit: function(hsb, hex, rgb, el, parent) {
                                    $(el).val('#' + hex);
                                    $(el).ColorPickerHide();
                                },
                                onBeforeShow: function () {
                                    $(this).ColorPickerSetColor(this.value);
                                }
                            }).bind('keyup', function(){
                                $(this).ColorPickerSetColor(this.value.replace('#', ''));
                            });
                        });
                    </script>
                    """ % ("id_%s" % name,)

        super_render = super(ColorPickerWidget, self).render(name, value, attrs)
        return mark_safe(u"%s%s" % (super_render, script))
