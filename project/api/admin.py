from django.contrib import admin

# Register your models here.

from project.api.models import Airport, Country, Flight

admin.site.register(Airport)
admin.site.register(Country)
admin.site.register(Flight)

