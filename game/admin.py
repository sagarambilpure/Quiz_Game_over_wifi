from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','password','gamingname']

class AnswerAdmin(admin.ModelAdmin):
    #fields=['bid','cid','sid_end','sid_start','uid']
    list_display=['uid','question_number','time']
    search_fields=['uid'] #to add search fields
    list_filter=['question_number','uid'] #to add filter functionality


admin.site.register(UserOfApp,UserAdmin)
admin.site.register(Answer,AnswerAdmin)
