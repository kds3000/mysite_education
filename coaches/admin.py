from django.contrib import admin
from .models import Coach

class CoachAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'gender', 'skype', 'description', 'get_is_staff' )
    list_filter = ('user__is_staff',)
    
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Name'
        
    def get_last_name(self, obj):
        return obj.user.last_name     
    get_last_name.short_description = 'Surname'
    
    def get_is_staff(self, obj):
        return obj.user.is_staff
    get_is_staff.short_description = 'Staff'    
        
admin.site.register(Coach, CoachAdmin)
