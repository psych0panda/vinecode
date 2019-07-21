from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from .permission import IsOwnerOrReadOnly
from .serializers import NoteSerializer, UserSerializer
from .models import Note


@api_view(['GET'])
def root_api(request, format=None):
    return Response({
        'users': reverse('notes:user-list', request=request, format=format),
        'notes': reverse('notes:note-list', request=request, format=format),
    })


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        return Note.objects.all().filter(owner=self.request.user)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().filter(username=self.request.user)
