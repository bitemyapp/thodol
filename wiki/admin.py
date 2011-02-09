from wiki.models import Page, Record
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_changed',)
    fields = ('name', 'content')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_changed', 'record_of')

admin.site.register(Page, PageAdmin)
admin.site.register(Record, RecordAdmin)