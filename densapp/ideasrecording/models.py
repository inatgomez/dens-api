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

    fields = [
        ('id',
         models.AutoField(
             auto_created = True,
             primary_key = True,
             serialize = False,
             verbose_name = 'ID'
         ))
    ]

    content = models.TextField()
    title = models.CharField(max_length=100)
    category = models.Choices(choices=categories)
    project_id = models.ForeignKey("project.unique_id")

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