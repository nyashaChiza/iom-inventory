from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    ordering = ('name',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'role', 'is_staff', 'is_active', 'created', 'updated')
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('email', 'username')
    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Register the models with the admin site
admin.site.register(Role, RoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)