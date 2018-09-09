"""Our API Serializers"""

from django.contrib.auth.models import User
from rest_framework import serializers
from dependency.models import Tags, Tasks, Successors, Predecessors, Movie, Book


class MovieSerializer(serializers.ModelSerializer):
    """Movie  Serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        model = Movie
        fields = ('url', 'id',
                  'title', 'rating', 'description', 'director',
                  'links','picture','release_date','production_company',
                  'motto','genre','cast','video','violence','nudity','horror',
                  'mpaa_rating','trivia'
                  )

class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        model = Book
        fields = ('url', 'id','title','authors',
                  'subgenre','description','thumbnail','release_date','tags',
                  'editions','goodreads','isbn','asin'
                 )

class PredecessorSerializer(serializers.ModelSerializer):
    """Predecessor Serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        """The Predecessor serializer"""
        model = Predecessors

        fields = ('url', 'id',
                  'predecessor_source_task',
                  'predecessor_target_task',
                  'confidence',
                  'document',
                  'comment',
                  'owner'
                 )

class SuccessorSerializer(serializers.ModelSerializer):
    """Successor Serializer"""
    class Meta: # pylint: disable=too-few-public-methods
        """The Successor serializer"""
        model = Successors

        fields = ('url', 'id',
                  'successor_source_task',
                  'successor_target_task',
                  'confidence',
                  'document',
                  'comment',
                  'owner'
                 )


class TaskSerializer(serializers.ModelSerializer):
    """Task Serializer"""

    class Meta: # pylint: disable=too-few-public-methods
        """The Task serializer"""
        model = Tasks
        fields = ('url', 'id', 'name', 'document', 'owner',
                  'successors', 'predecessors', 'tags',
                  'costLow', 'costHi', 'duration',
                  'confidence', 'TRL', 'editable', 'startdate',
                  'enddate', 'isp_columns', 'legacyUrl', 'elementID')

class TagSerializer(serializers.ModelSerializer):
    """The Tag serializer"""

    class Meta: # pylint: disable=too-few-public-methods
        """The Tag Serializer"""
        model = Tags
        fields = ('id', 'name', 'description')


class UserSerializer(serializers.ModelSerializer): # pylint: disable=missing-docstring
    tasks = serializers.StringRelatedField(many=True)

    class Meta: # pylint: disable=missing-docstring, too-few-public-methods
        model = User
        fields = ('url', 'id', 'username', 'tasks')
