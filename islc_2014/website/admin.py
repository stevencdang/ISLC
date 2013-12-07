from django.contrib import admin
from website.models import Registration


class RegAdmin(admin.ModelAdmin):
    list_display = ('slc',
                    'last_name',
                    'first_name',
                    'university',
                    'department',
                    'email')

admin.site.register(Registration, RegAdmin)
