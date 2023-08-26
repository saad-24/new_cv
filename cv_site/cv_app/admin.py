from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Company)
admin.site.register(Skills)
admin.site.register(user_data)
admin.site.register(Education)
admin.site.register(Certifications)

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    # Restrict access to admin users only
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

