from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer, QuestionBookmark, AnswerBookmark


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionBookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionBookmark
        fields = '__all__'


class AnswerBookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerBookmark
        fields = '__all__'
