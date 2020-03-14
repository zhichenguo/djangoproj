from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    questioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["create_time"]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["create_time"]


class QuestionBookmark(models.Model):
    bookmarked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_bookmarks')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_bookmarks')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bookmarked_by', 'question'], name='unique_question_bookmarks')
        ]


class AnswerBookmark(models.Model):
    bookmarked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_bookmarks')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_bookmarks')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['bookmarked_by', 'answer'], name='unique_answer_bookmarks')
        ]

