from django.contrib import admin

from .models import *

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'realname', 'useremail')
#admin.site.register(Teacher)
admin.site.register(Account, AccountAdmin)
