"""restapiproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import QuestionAPIView, AnswerAPIView, QuestionBookmarkAPIView, AnswerBookmarkAPIView

# app_name = 'webforum'

urlpatterns = [
    path('question/<int:id>/', QuestionAPIView.as_view(), name='question_detail'),
    path('question/', QuestionAPIView.as_view(), name="question_list"),
    path('answer/<int:id>/', AnswerAPIView.as_view(), name='answer_detail'),
    path('answer/', AnswerAPIView.as_view(), name='answer_list'),
    path('questionbookmark/<int:id>/', QuestionBookmarkAPIView.as_view(), name='questionbookmark_detail'),
    path('questionbookmark/', QuestionBookmarkAPIView.as_view(), name='questionbookmark_list'),
    path('answerbookmark/<int:id>/', AnswerBookmarkAPIView.as_view(), name='answerbookmark_detail'),
    path('answerbookmark/', AnswerBookmarkAPIView.as_view(), name='answerbookmark_list'),
]
