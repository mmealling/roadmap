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
router.register(r'api/v1/tasks', views.TaskViewSet)
router.register(r'api/v1/tags', views.TagViewSet)
router.register(r'api/v1/users', views.UserViewSet)
router.register(r'api/v1/predecessors', views.PredecessorViewSet)
router.register(r'api/v1/successors', views.SuccessorViewSet)
router.register(r'api/v1/movies',views.MovieViewSet)
router.register(r'api/v1/books',views.BookViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^(?P<path>.*)$', views.HomePageView.as_view())
]
