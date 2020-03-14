from django.test import TestCase
from django.urls import reverse, resolve
from ..views import QuestionAPIView, AnswerAPIView, QuestionBookmarkAPIView, AnswerBookmarkAPIView


# Testing for urls that are resolved
class TestUrls(TestCase):

    def test_question_list_urls(self):
        url = reverse('question_list')
        self.assertEquals(resolve(url).func.view_class, QuestionAPIView)

    def test_question_detail_urls(self):
        url = reverse('question_detail', kwargs={'id': 1})
        self.assertEquals(resolve(url).func.view_class, QuestionAPIView)

    def test_answer_list_urls(self):
        url = reverse('answer_list')
        self.assertEquals(resolve(url).func.view_class, AnswerAPIView)

    def test_answer_detail_urls(self):
        url = reverse('answer_detail', kwargs={'id': 1})
        self.assertEquals(resolve(url).func.view_class, AnswerAPIView)

    def test_questionbookmark_list_urls(self):
        url = reverse('questionbookmark_list')
        self.assertEquals(resolve(url).func.view_class, QuestionBookmarkAPIView)

    def test_questionbookmark_detail_urls(self):
        url = reverse('questionbookmark_detail', kwargs={'id': 1})
        self.assertEquals(resolve(url).func.view_class, QuestionBookmarkAPIView)

    def test_answerbookmark_list_urls(self):
        url = reverse('answerbookmark_list')
        self.assertEquals(resolve(url).func.view_class, AnswerBookmarkAPIView)

    def test_answerbookmark_detail_urls(self):
        url = reverse('answerbookmark_detail', kwargs={'id': 1})
        self.assertEquals(resolve(url).func.view_class, AnswerBookmarkAPIView)
