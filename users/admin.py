from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'first_name','last_name')
    list_filter = ('is_active',)
    ordering = ('username',)
    search_fields = ('username',)
    


admin.site.register(User,UserAdmin)







