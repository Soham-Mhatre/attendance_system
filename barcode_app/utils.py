# utils.py

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models
from django.urls import reverse


# Function to create a new table dynamically
def create_dynamic_table(table_name, fields=None, app_label='', module='', options=None, admin_opts=None):
    class Meta:
        pass

    if app_label:
        setattr(Meta, 'app_label', app_label)

    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    attrs = {'__module__': module, 'Meta': Meta}

    if fields:
        attrs.update(fields)

    model = type(table_name, (models.Model,), attrs)

    if admin_opts is not None:
        class Admin(ModelAdmin):
            pass

        for key, value in admin_opts.items():
            setattr(Admin, key, value)

        admin_attrs = {'__module__': module, 'Meta': Meta}
        admin_attrs.update(admin_opts)
        admin = type('Admin%s' % table_name, (admin.ModelAdmin,), admin_attrs)
        admin_instance = admin(model, None)
        admin.site.register(model, admin_instance)  # Registering the model in the admin

    return model
