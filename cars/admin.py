from django.contrib import admin

from cars.models import Trim, Model, Make, PaymentType, Payment, PaymentTerm

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Trim)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(PaymentTerm)
