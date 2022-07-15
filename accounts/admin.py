from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *

# Register your models here:

admin.site.site_header='vendor '
admin.site.index_title='Welcome to Superadmin Panel'


class RegistrationAdmin(BaseUserAdmin):
    add_form=customUserCreationForm
    form=customeUserChangeForms 
    model=Registration
    list_display=('id','username','password','mobile_no')
    
    
admin.site.register(Registration,RegistrationAdmin)

