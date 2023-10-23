from django.contrib import admin
from .models import EnrollFormData

# class enrolldataAdmin(admin.ModelAdmin):
#     list_display=("regno","name","fname","mname","dob","email","phone","address","city","gender","photo","btime","pay_mode","name_on_card","card_no","expiry","cvv")

# admin.site.register(enrolldata,enrolldataAdmin)

class EnrollFormDataAdmin(admin.ModelAdmin):
    list_display=('regno','name','fname','mname','dob','email','phone','address','city','gender','photo','btime','pay_mode','name_on_card','card_no','expiry','cvv')

admin.site.register(EnrollFormData,EnrollFormDataAdmin)
