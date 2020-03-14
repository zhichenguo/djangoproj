from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Question, Answer, QuestionBookmark, AnswerBookmark
from .serializers import QuestionSerializer, AnswerSerializer, QuestionBookmarkSerializer, AnswerBookmarkSerializer


class QuestionAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)


class AnswerAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    # def put(self, request, id=None):
    #     return self.update(request, id)


class QuestionBookmarkAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                              mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionBookmarkSerializer
    lookup_field = 'id'

    def get_queryset(self):
        # only list the question bookmarks that created by the current user
        return QuestionBookmark.objects.filter(bookmarked_by=self.request.user)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)


class AnswerBookmarkAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                            mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerBookmarkSerializer
    lookup_field = 'id'

    def get_queryset(self):
        # only list the answer bookmarks that created by the current user
        return AnswerBookmark.objects.filter(bookmarked_by=self.request.user)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)
