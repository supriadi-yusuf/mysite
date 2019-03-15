from django.contrib import admin

from . import models

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    ( None,               {'fields': ['question_text']}),
    ( 'Date Information', {'fields': ['pub_date']}),
    ]

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
