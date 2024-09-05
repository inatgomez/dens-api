import uuid
from django.db import models

class Idea(models.Model):
    """
    Model representing an idea for a project.
    """

    categories = [
        'character',
        'plot',
        'setting',
        'theme'
    ]

    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    title = models.CharField(max_length=100)
    category = models.Choices(choices=categories)
    project_id = models.ForeignKey("project.unique_id")
    date_added = models.DateTimeField("date_created")
    date_updated = models.DateTimeField("date_updated")

class Project(models.Model):

    fiction_genre = [
        'Romance',
        'Mistery',
        'Sci-fi',
        'Fantasy',
        'Action',
        'Drama',
        'Detective',
        'Horror',
        'Coming of age',
        'Comedy'
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    genres = models.Choices(choices=fiction_genre)