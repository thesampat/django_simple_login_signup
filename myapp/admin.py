from django.contrib import admin
from .models import Custom_User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Custom_User
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Personal info',
            {
                'fields': (
                    'DOB',
                )
            }
        )
    )

admin.site.register(Custom_User, CustomUserAdmin)
