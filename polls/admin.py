from django.contrib import admin
from polls.models import Question, Choice


admin.site.site_header = "Polls Administration"
admin.site.site_title = "Hello"
admin.site.index_title = "Welcome To Polls Administration"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Published', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
