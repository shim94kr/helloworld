__author__ = 'cloud'
from django.contrib import admin
from polls.models import Choice,Poll

admin.site.register(Poll)
admin.site.register(Choice)

"""
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra=3

class PollAdmin (admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)
"""