"""The basic models for a dependency tree with costs and time"""

from django.contrib.postgres.fields import JSONField
from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

class Tags(models.Model):
    """All items have tags"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User',
                              related_name='tags',
                              null=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Movie(models.Model):
    """A movie"""
    title = models.CharField(max_length=100)
    elementID = models.CharField(max_length=200,null=True, blank=True)
    tmdb_id = models.CharField(max_length=200,null=True, blank=True)
    
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

    STARS = (
        (ONE_STAR, '*'),
        (TWO_STARS, '**'),
        (THREE_STARS, '***'),
        (FOUR_STARS, '**** '),
        (FIVE_STARS, '*****')
    )
    rating = models.SmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=200,null=True, blank=True)
    links = models.URLField(max_length=1000,null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    production_company = models.CharField(max_length=200,null=True, blank=True)
    motto = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=200,null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    video = models.URLField(max_length=1000,null=True, blank=True)
    violence = models.SmallIntegerField(choices=STARS, null=True, blank=True)
    nudity = models.SmallIntegerField(choices=STARS, null=True, blank=True)
    horror = models.SmallIntegerField(choices=STARS, null=True, blank=True)

    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    N_A = "N/A"

    MPAA_RATING = (
        (G,'G'),
        (PG,'PG'),
        (PG_13, 'PG-13'),
        (R,'R'),
        (N_A,'N/A')
    )

    mpaa_rating = models.CharField(max_length=5, choices=MPAA_RATING, null=True)
    trivia = models.TextField(null=True, blank=True)

class Book(models.Model):
    """ A book """
    title = models.CharField(max_length=200)
    elementID = models.CharField(max_length=200,null=True, blank=True)
    librarything_id = models.CharField(max_length=200,null=True, blank=True)
    authors = JSONField(null=True)  
    genre = JSONField(null=True)
    subgenre = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = JSONField(null=True)
    release_date = models.DateField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    editions = models.TextField(null=True, blank=True)
    goodreads = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=100,null=True, blank=True)
    asin = models.CharField(max_length=100,null=True, blank=True)

class Successors(models.Model):
    """The through class for a successor task so the edge can be annotated"""
    successor_source_task = models.ForeignKey('Tasks', related_name='successor_source_task', on_delete=models.DO_NOTHING)
    successor_target_task = models.ForeignKey('Tasks', related_name='successor_target_to_task', on_delete=models.DO_NOTHING)
    confidence = models.DecimalField(max_digits=2, decimal_places=2)
    document = JSONField(null=True)
    comment = models.TextField
    owner = models.ForeignKey('auth.User',
                              related_name='successors',
                              null=True,
                              on_delete=models.SET_NULL)

class Predecessors(models.Model):
    """The through class for a predecessor so the edge can be annotated"""
    predecessor_source_task = models.ForeignKey('Tasks', related_name='predecessor_source_task', on_delete=models.DO_NOTHING)
    predecessor_target_task = models.ForeignKey('Tasks', related_name='predecessor_target_task', on_delete=models.DO_NOTHING)
    confidence = models.DecimalField(max_digits=2, decimal_places=2)
    document = JSONField(null=True)
    comment = models.TextField
    owner = models.ForeignKey('auth.User',
                              related_name='predecessors',
                              null=True,
                              on_delete=models.SET_NULL)    

class Vendor(models.Model):
    """The through class for a vendor/customer relationship"""

class Customer(models.Model):
    """The through class for a vendor/customer relationship"""

class Tasks(models.Model):
    """The item"""
    name = models.CharField(max_length=200)
    document = JSONField(null=True, blank=True)
    successor = models.ManyToManyField("self", blank=True, through='Successors', related_name='successors', symmetrical=False)
    predecessor = models.ManyToManyField("self", blank=True, through='Predecessors', related_name='predecessors', symmetrical=False)
    tags = models.ManyToManyField(Tags, blank=True)
    costLow = MoneyField(max_digits=15, decimal_places=2, default_currency='USD')
    costHi = MoneyField(max_digits=15, decimal_places=2, default_currency='USD')
    duration = models.IntegerField()
    owner = models.ForeignKey('auth.User',
                              related_name='tasks',
                              null=True, blank=True,
                              on_delete=models.SET_NULL)

    editable = models.BooleanField(default=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    confidence = models.DecimalField(max_digits=2, decimal_places=2, null=True)

    TRL_1 = 1
    TRL_2 = 2
    TRL_3 = 3
    TRL_4 = 4
    TRL_5 = 5
    TRL_6 = 6
    TRL_7 = 7
    TRL_8 = 8
    TRL_9 = 9
    TRLS = (
        (TRL_1, '1. Basic principles observed and reported'),
        (TRL_2, 'Technology concept and/or application formulated'),
        (TRL_3, 'Analytical and experimental critical function and/or characteristic proof of concept'),
        (TRL_4, 'Component and/or breadboard validation in laboratory environment '),
        (TRL_5, 'Component and/or breadboard validation in relevant environment'),
        (TRL_6, 'System/subsystem model or prototype demonstration in a relevant environment (ground or space)'),
        (TRL_7, 'System prototype demonstration in a space environment'),
        (TRL_8, 'Actual system completed and "flight qualified" through test and demonstration (ground or space)'),
        (TRL_9, 'Actual system "flight proven" through successful mission operations'),
    )
    TRL = models.SmallIntegerField(choices=TRLS, null=True)

    TRANSPORT = 'Transport (Earth-to-Orbit)'
    INFRASTRUCTURE = 'Infrastructure'
    SUPPORT_ELEMENTS = 'Critical Path Support Elements'
    EMERGING = 'R&D / Emerging Technologies'
    ROBOTS = 'Robotic Exploration'
    PROPULSION = 'Propulsion Systems / Planetary Expansion'
    IN_SPACE_TRANSPORT = 'In-space Reusable Transport'
    ISP_COLUMNS = (
        (TRANSPORT, 'Transport (Earth-to-Orbit)'),
        (INFRASTRUCTURE, 'Infrastructure'),
        (SUPPORT_ELEMENTS, 'Critical Path Support Elements'),
        (EMERGING, 'R&D / Emerging Technologies'),
        (ROBOTS, 'Robotic Exploration'),
        (PROPULSION, 'Propulsion Systems / Planetary Expansion'),
        (IN_SPACE_TRANSPORT, 'In-space Reusable Transport'),
    )
    isp_columns = models.CharField(
        max_length=100,
        choices=ISP_COLUMNS,
        default=TRANSPORT
    )
    elementID = models.CharField(max_length=200)
    legacyUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
