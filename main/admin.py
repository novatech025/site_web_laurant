from django.contrib import admin
from .models import *
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('sable', 'name', 'description','image')
    search_fields = ['name', ]

class RealisationAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'description','date','image')
    search_fields = ['title', ]

class SableAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'description')
    search_fields = ['type', ]

admin.site.register(Sable,SableAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Realisation,RealisationAdmin)

ets='QUALISABLE'
admin.site.site_title=ets
admin.site.site_header=ets
admin.site.index_title=ets