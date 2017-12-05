from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from ..models import Snippet
from ..permissions import IsOwnerOrReadOnly
from ..serializers import SnippetHyperLinkedSerializer, UserHyperLinkedSerializer


class SnippetHyperLinkedList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetHyperLinkedSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetHyperLinkedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetHyperLinkedSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserHyperLinkedList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserHyperLinkedSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserHyperLinkedDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserHyperLinkedSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
