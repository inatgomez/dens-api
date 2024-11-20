import uuid
from django.db import models
from django.utils import timezone

class Idea(models.Model):
    """
    Model representing an idea for a story project.
    """
    class Category(models.TextChoices):

        PLOT = 'PLOT', 'Plot'
        CHARACTER = 'CHARACTER', 'Character'
        THEME = 'THEME', 'Theme'
        SETTING = 'SETTING', 'Setting'
        RESEARCH = 'RESEARCH', 'Research'
        RANDOM = 'RANDOM', 'Random'

    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    title = models.CharField(max_length=100, blank=True, default="Untitled")
    category = models.CharField(max_length=9, choices=Category.choices, default=Category.RANDOM)
    project = models.ForeignKey("Project", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    """
    Model representing a story project.
    """

    class Genre(models.TextChoices):

        ROMANCE = 'ROMANCE', 'romance'
        MISTERY = 'MISTERY', 'mistery'
        SCIFI = 'SCI-FI', 'sci-fi'
        FANTASY = 'FANTASY', 'fantasy'
        ACTION = 'ACTION', 'action'
        DRAMA = 'DRAMA', 'drama'
        DETECTIVE = 'DETECTIVE', 'detective'
        HORROR = 'HORROR', 'horror'
        AGE = 'COMING OF AGE', 'coming of age'
        COMEDY = 'COMEDY', 'comedy'
        NONE = 'NONE', 'none'

    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    main_genre = models.CharField(max_length=13, choices=Genre.choices)
    mix_genre = models.CharField(max_length=13, choices=Genre.choices, blank=True)

    def __str__(self):
        return self.name