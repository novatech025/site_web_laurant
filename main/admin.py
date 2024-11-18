from django.contrib import admin
from .models import *
# Register your models here.


class RealisationAdmin(admin.ModelAdmin):
    list_display = ('sable', 'title', 'description','date','image')
    search_fields = ['title', ]

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'comment','stars','photo')
    search_fields = ['name', ]
class Message_UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','date_send')
    search_fields = ['name', ]

admin.site.register(Realisation,RealisationAdmin)
admin.site.register(Message_User,Message_UserAdmin)
admin.site.register(Testimonial,TestimonialAdmin)

ets='QUALISABLE'
admin.site.site_title=ets
admin.site.site_header=ets
admin.site.index_title=ets
