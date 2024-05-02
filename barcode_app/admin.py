from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TimeSlot
from .models import *


admin.site.register(TimeSlot)
admin.site.register(Teachers)
admin.site.register(SGs1s2)
admin.site.register(Sg0001s101s102)
admin.site.register(barcode_app_s3s4)
admin.site.register(Rb0002s13s14)
admin.site.register(Rb0002s91s92)

admin.site.register(s3s4)

# admin.py
from django.contrib import admin
from .models import TimeSlot, Teachers, Barcode


class DynamicTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'present')

admin.site.register(DynamicTable)

