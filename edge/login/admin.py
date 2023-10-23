from django.contrib import admin
from .models import loginac

class loginacAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_no')

admin.site.register(loginac,loginacAdmin)
