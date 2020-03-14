from django.contrib import admin
from .models import Question, Answer, QuestionBookmark, AnswerBookmark
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionBookmark)
admin.site.register(AnswerBookmark)
