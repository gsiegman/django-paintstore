django-paintstore
==================

``django-paintstore`` is a Django app that integrates `jQuery ColorPicker`_ with the Django admin


Quickstart
----------

#. Install the app with your preferred Python packaging utility, for example::

    pip install django-paintstore

#. Add the application to the ``INSTALLED_APPS`` in settings.py::

        INSTALLED_APPS = (
            # ...
            'paintstore',
        )

#. Add a ColorPickerField to your model::
		
		# ...
		from paintstore.fields import ColorPickerField

		class ColorfulModel(models.Model):
			title = models.CharField(max_length=25)
			color = ColorPickerField()

#. Optional: Edit colors directly in your model's change list admin::

		class ColorfulModelAdmin(admin.ModelAdmin):
			list_display = ["title", "color",]
			list_editable = ["color",]


.. _`jQuery ColorPicker`: https://github.com/Belelros/jQuery-ColorPicker