from django.contrib import admin
from .models import center,center_name, distribution, chennai
# Register your models here.

class centerAdmin(admin.ModelAdmin):
    list_display=['name','allotted','date']

admin.site.register(center, centerAdmin)

class center_nameAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(center_name, center_nameAdmin)

class distributionAdmin(admin.ModelAdmin):
    list_display=['imei','tablet_id','allotted_to','start_date','end_date','complete','condition']
    list_editable=['start_date','end_date','complete','condition']

admin.site.register(distribution, distributionAdmin)

class chennaiAdmin(admin.ModelAdmin):
    list_display=['imei','t_id','date','received']
    list_editable=['received']

admin.site.register(chennai, chennaiAdmin)