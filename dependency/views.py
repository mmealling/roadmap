"""Dependency and User views"""
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from django.shortcuts import render
from django.views.generic import TemplateView
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

from dependency.models import Tags, Tasks, Predecessors, Successors
from dependency.permissions import IsOwnerOrReadOnly
from dependency.serializers import TagSerializer, TaskSerializer, UserSerializer, PredecessorSerializer, SuccessorSerializer

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class PredecessorViewSet(viewsets.ModelViewSet):
    """This viewset represents a connection to a predecssor task"""
    queryset = Predecessors.objects.all()
    serializer_class = PredecessorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SuccessorViewSet(viewsets.ModelViewSet):
    """This viewset represents a connection to a predecssor task"""
    queryset = Successors.objects.all()
    serializer_class = SuccessorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    pagination_class = None
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
