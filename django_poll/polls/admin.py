from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):    
    # Question 추가 페이지 내 항목들의 순서 변경(지정)
    fieldsets = [
        ('Question title', {'fields' : [ 'question_text' ]}),
        ('Date information', {'fields': [ 'pub_date' ], 'classes': ['collapse']}),
    ]
    inlines = [ ChoiceInline ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = [ 'pub_date' ]
    search_fields = [ 'question_text' ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
