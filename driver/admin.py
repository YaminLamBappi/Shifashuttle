from django.contrib import admin
from .models import Driver, Ambulance, ContactMessage
from .models import  HireRequest, Message

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'model', 'capacity', 'status', 'location')
    search_fields = ('registration_number', 'model')
    list_filter = ('status', 'capacity')
    ordering = ('registration_number',)

class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')
    ordering = ('user',)

class HireRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'ambulance', 'current_location', 'destination', 'status', 'created_at')
    search_fields = ('user__username', 'ambulance__registration_number', 'current_location', 'destination')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
    
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
    

admin.site.register(Ambulance, AmbulanceAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(HireRequest, HireRequestAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)


    

