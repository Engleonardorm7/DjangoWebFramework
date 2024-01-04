from django.contrib import admin
from .models import Logger, Person
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



# Register your models here.
# admin.site.register(Person)
# admin.site.register(Logger)
# admin.site.unregister(User)

# @admin.register(User)
# class NewAdmin(UserAdmin):
#     readonly_fields=[
#         'date_joined',
#         'last_login'
    
#     ]

#     def get_form(self, request, obj=None, **kwargs):
#         form=super().get_form(request, obj, **kwargs)
#         is_superuser=request.user.is_superuser

#         if not is_superuser:
#             form.base_field['usename'].disabled=True
#         return form
    
    
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name')    
    search_fields=('first_name__startswith',)