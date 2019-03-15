from django.contrib import admin

from . import models

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3 # add extra 3 choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ( None,               {'fields': ['question_text']}),
       ( 'Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(models.Question, QuestionAdmin)
