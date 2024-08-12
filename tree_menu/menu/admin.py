from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    ordering = ('menu_name', 'parent', 'order')

admin.site.register(MenuItem, MenuItemAdmin)