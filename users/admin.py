from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from users.models import User

class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')
    
admin.site.register(User, UserAdmin)