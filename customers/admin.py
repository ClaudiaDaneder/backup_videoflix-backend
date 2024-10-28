from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm
from .models import Customer

@admin.register(Customer)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomerCreationForm
    model = Customer

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'activation_token'
            )
        }),

        ('Personal info',{
            'fields': (
                'first_name',
                'last_name',
                'email'
            )
        }),

        ('Individual data', {
            'fields': (
                'street',
                'zip_code',
                'city',
                'country',
                'notes'
            )
        }),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        'classes': ('collapse',),
        }),

        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined'
            ),
        'classes': ('collapse',),
        }),

    )

    list_display = ('username', 'first_name', 'last_name', 'id', 'email')
    sortable_by = ('id', 'last_name')
