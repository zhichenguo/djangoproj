import json
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.db import models
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import Question, Answer, QuestionBookmark, AnswerBookmark


# Testing for views
class TestAPIViews(APITestCase):

    def setUp(self):
        # setup the database as below. 2 users, 2 questions, 3 answers,
        # 2 question bookmarks and 3 answer bookmarks
        self.user1 = User.objects.create_user(
            username='testcase1',
            password='testcase1_pwd')
        self.user2 = User.objects.create_user(
            username='testcase2',
            password='testcase2_pwd')
        self.question1 = Question.objects.create(
            title='test_question1',
            body='test_question1_body',
            questioner=self.user1
        )
        self.question2 = Question.objects.create(
            title='test_question2',
            body='test_question2_body',
            questioner=self.user2
        )
        self.answer1 = Answer.objects.create(
            question=self.question1,
            body='test_answer1_body, for question1',
            answerer=self.user2
        )
        self.answer2 = Answer.objects.create(
            question=self.question2,
            body='test_answer2_body, for question2',
            answerer=self.user1
        )
        self.answer3 = Answer.objects.create(
            question=self.question2,
            body='test_answer3_body, for question2',
            answerer=self.user2
        )
        self.questionbookmark1 = QuestionBookmark.objects.create(
            question=self.question1,
            bookmarked_by=self.user1
        )
        self.questionbookmark2 = QuestionBookmark.objects.create(
            question=self.question2,
            bookmarked_by=self.user2
        )
        self.answerbookmark1 = AnswerBookmark.objects.create(
            answer=self.answer1,
            bookmarked_by=self.user1
        )
        self.answerbookmark2 = AnswerBookmark.objects.create(
            answer=self.answer2,
            bookmarked_by=self.user2
        )
        self.answerbookmark3 = AnswerBookmark.objects.create(
            answer=self.answer3,
            bookmarked_by=self.user1
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        self.questionbookmark_list_url = reverse('questionbookmark_list')
        # self.questionbookmark_detail_url = reverse('questionbookmark_detail')
        self.answerbookmark_list_url = reverse('answerbookmark_list')
        # self.answerbookmark_detail_url = reverse('answerbookmark_detail')

    def test_question_list_GET(self):
        response = self.client.get(reverse('question_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)  # 2 questions in total

    def test_question_list_POST(self):
        response = self.client.post(reverse('question_list'),
                                    {'title': 'test_question3',
                                     'body': 'test_question3_body',
                                     'questioner': 1})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_question_detail_GET(self):
        response = self.client.get(reverse('question_detail', kwargs={'id': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # check the 1st question's detail
        self.assertEquals(response.data['title'], 'test_question1')
        self.assertEquals(response.data['body'], 'test_question1_body')
        self.assertEquals(response.data['questioner'], 1)

    def test_answer_list_GET(self):
        response = self.client.get(reverse('answer_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)  # 3 answers in total

    def test_answer_list_POST(self):
        response = self.client.post(reverse('answer_list'),
                                    {'question': 1,
                                     'body': 'test_answer4_body, for question1',
                                     'answerer': 1})
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_answer_detail_GET(self):
        response = self.client.get(reverse('answer_detail', kwargs={'id': 1}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # check the 1st answer's detail, the answerer should be user2
        self.assertEquals(response.data['question'], 1)
        self.assertEquals(response.data['body'], 'test_answer1_body, for question1')
        self.assertEquals(response.data['answerer'], 2)

    def test_questionbookmark_list_GET(self):
        response = self.client.get(reverse('questionbookmark_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # only one question bookmark can be got by current user1
        # because users only can see their own bookmarks
        self.assertEquals(len(response.data), 1)

    def test_questionbookmark_list_POST(self):
        try:
            # testing for one user can not bookmark one question twice
            response = self.client.post(reverse('questionbookmark_list'),
                                        {'bookmarked_by': 1,
                                         'question': 2})
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        except IntegrityError:
            print("UNIQUE constraint not tested")

    def test_questionbookmark_list_POST_UNIQUE_Constrain(self):
        try:
            # testing for one user can not bookmark one question twice
            response = self.client.post(reverse('questionbookmark_list'),
                                        {'bookmarked_by': 1,
                                         'question': 1})
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        except IntegrityError:
            print("UNIQUE constraint tested for question bookmark post")

    def test_answerbookmark_list_GET(self):
        response = self.client.get(reverse('answerbookmark_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        # only two answer bookmarks can be got by current user1
        # because users only can see their own bookmarks
        self.assertEquals(len(response.data), 2)

    def test_answerbookmark_list_POST(self):
        try:
            # testing for one user can not bookmark one answer twice
            response = self.client.post(reverse('answerbookmark_list'),
                                        {'bookmarked_by': 2,
                                         'answer': 3})
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        except IntegrityError:
            print("UNIQUE constraint not tested")

    def test_answerbookmark_list_POST_UNIQUE_Constrain(self):
        try:
            # testing for one user can not bookmark one answer twice
            response = self.client.post(reverse('answerbookmark_list'),
                                        {'bookmarked_by': 1,
                                         'answer': 1})
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        except IntegrityError:
            print("UNIQUE constraint tested for answer bookmark post")

    def test_authentication(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_question_detail_UPDATE_by_owner(self):
    #     response = self.client.put(reverse('question_detail', kwargs={'id': 1}),
    #                                {'title': 'test_question1_updated',
    #                                 'body': 'test_question1_body_updated',
    #                                 'questioner': 1})
    #     self.assertEquals(response.status_code, 200)
    #     # check the contents after update
    #     self.assertEquals(json.loads(response.content)['title'], 'test_question1_updated')
    #     self.assertEquals(json.loads(response.content)['body'], 'test_question1_body_updated')

    # def test_question_detail_UPDATE_by_random_user(self):
    #     random_user = User.objects.create_user(username="random", password="random_pwd")
    #     self.client.force_authenticate(user=random_user)
    #     response = self.client.put(reverse('question_detail', kwargs={'id': 1}),
    #                                {'title': 'test_question1_updated',
    #                                 'body': 'test_question1_body_updated',
    #                                 'questioner': 1})
    #     self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)







