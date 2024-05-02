"""
URL configuration for barcode_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from barcode_app.views import *
from django.urls import path
from barcode_app.views import *


urlpatterns = [
    path('', home, name='home'),
    path('input/', barcode_input, name='barcode_input'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name="login"),
    path('barcode_display/', barcode_display, name='barcode_display'),
    path('scan_barcode/', scan_barcode, name='scan_barcode'),
    path('barcode_display/<str:barcode_data>/<str:scan_time>/<str:day>/<str:table_name>/', barcode_display, name='barcode_display'),
    path('select/',select,name="select"),
    path('start_scan/',start_scan,name="start_scan"),
    path('attendance/', attendance_record, name='attendance_record'),
]
