from django.contrib import admin

from .models import Cars, types, Reservation


admin.site.register(Cars)
admin.site.register(types)
admin.site.register(Reservation)