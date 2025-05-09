import uuid
from django.db import models
from django.utils import timezone
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from users.models import UserAccount

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
    project = models.ForeignKey("Project", on_delete=models.PROTECT, related_name='ideas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=["search_vector"], name="idea_search_idx"),
        ]

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
    main_genre = models.CharField(max_length=13, choices=Genre.choices, blank=True)
    mix_genre = models.CharField(max_length=13, choices=Genre.choices, blank=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name