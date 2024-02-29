from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Cart,Address
from .forms import UserChangeForm,UserCreationForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name" ,'phone']}),
        ("Permissions", {"fields": ["is_admin","is_active"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","phone", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)




class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'Quantity', 'Pid']

admin.site.register(Cart, CartAdmin)



class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'Name', 'Phone']

admin.site.register(Address, AddressAdmin)