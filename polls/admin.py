from django.contrib import admin

from . import models

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3 # add extra 3 choices

class QuestionAdmin(admin.ModelAdmin):
    ####### for insert / update question ########
    fieldsets = [
       ( None,               {'fields': ['question_text']}),
       ( 'Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    ###### for display item list #######
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(models.Question, QuestionAdmin)
