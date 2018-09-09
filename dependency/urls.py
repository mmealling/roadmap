"""Using Simples from the router for the ViewSets"""

from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from dependency import views
import logging

logger = logging.getLogger(__name__)

# Create a router and register our viewsets with it.


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
      logger.info('In OptionalSlashRouter')
      self.trailing_slash = '/?'
      super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'predecessors', views.PredecessorViewSet)
router.register(r'successors', views.SuccessorViewSet)
router.register(r'movies',views.MovieViewSet)
router.register(r'books',views.BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
    url(r'^', include(router.urls))
]
