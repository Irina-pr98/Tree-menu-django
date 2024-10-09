from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent', 'is_active')
    list_filter = ('is_active',)
    # search_fields = ('name',)
    # raw_id_fields = ('parent',)
    
admin.site.register(MenuItem, MenuItemAdmin)
