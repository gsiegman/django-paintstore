from django.db.models import CharField

from paintstore.widgets import ColorPickerWidget


class ColorPickerField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 7
        super(ColorPickerField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.update({"widget": ColorPickerWidget})
        return super(ColorPickerField, self).formfield(**kwargs)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^paintstore\.fields\.ColorPickerField"])
except ImportError:
    pass
