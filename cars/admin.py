from django.contrib import admin

from cars.models import Trim, Model, Make

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Trim)
