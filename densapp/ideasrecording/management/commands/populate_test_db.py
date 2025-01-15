from django.core.management.base import BaseCommand
from django.utils import timezone
from ideasrecording.models import Project, Idea
from django.contrib.postgres.search import SearchVector
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def generate_random_date(self, start_date, end_date):
        """Generate a random datetime between start_date and end_date"""
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randrange(days_between)
        random_seconds = random.randrange(86400)  # seconds in a day
        return start_date + timedelta(days=random_days, seconds=random_seconds)

    def generate_content(self, category):
        """Generate sophisticated content based on category"""
        
        plot_elements = {
            'discoveries': [
                "an ancient prophecy written in starlight",
                "a hidden door beneath the city's oldest library",
                "a message encoded in their own DNA",
                "a map that changes based on the reader's fears",
                "a device that can alter memories"
            ],
            'consequences': [
                "unleashing an ancient force that was better left dormant",
                "questioning everything they believed about their world",
                "starting a chain reaction that threatens reality itself",
                "discovering their true heritage and destiny",
                "gaining powers they're not ready to control"
            ],
            'events': [
                "the sudden disappearance of all digital technology",
                "the merging of parallel universes",
                "the awakening of dormant genes in the population",
                "the arrival of beings from another dimension",
                "the discovery of time loops in specific locations"
            ],
            'results': [
                "society splitting into opposing factions",
                "a fundamental change in how magic works",
                "the breakdown of physical laws in certain areas",
                "mass migration to underground cities",
                "the emergence of new human abilities"
            ]
        }

        character_elements = {
            'traits': [
                "can see threads of probability",
                "never casts a shadow",
                "speaks in riddles that predict the future",
                "changes appearance based on others' expectations",
                "can taste lies"
            ],
            'secrets': [
                "their role in an ancient prophecy",
                "their true age and origin",
                "their ability to manipulate time",
                "their connection to parallel worlds",
                "their deal with cosmic entities"
            ],
            'characteristics': [
                "their unnatural intuition",
                "their perfect memory",
                "their ability to see patterns",
                "their resistance to magic",
                "their influence over technology"
            ],
            'flaws': [
                "inability to remember their own past",
                "tendency to accidentally alter reality",
                "compulsion to tell the absolute truth",
                "fear of their own potential",
                "difficulty distinguishing dreams from reality"
            ]
        }

        setting_elements = {
            'conditions': [
                "time flows differently in each district",
                "thoughts become visible as colored mist",
                "emotions affect the physical environment",
                "memories can be traded like currency",
                "dreams manifest as physical objects"
            ],
            'features': [
                "buildings that rearrange themselves at night",
                "streets that lead to different times",
                "plants that feed on sound",
                "weather that responds to collective mood",
                "shadows that move independently"
            ],
            'locations': [
                "a city built in the spaces between moments",
                "a library where books write themselves",
                "a market that only exists at twilight",
                "a forest where physics works backwards",
                "an underground network of emotion-powered trains"
            ],
            'atmospheres': [
                "perpetual aurora borealis",
                "crystallized time fragments floating in the air",
                "shifting gravity patterns",
                "visible ley lines crisscrossing the sky",
                "echoes of future events"
            ]
        }

        theme_elements = {
            'moral_questions': [
                "whether the ends justify the means",
                "if truth is more important than happiness",
                "how much freedom should be sacrificed for security",
                "whether revenge can bring peace",
                "if knowledge is always worth its price",
                "whether power inevitably corrupts",
                "if loyalty to family should override moral principles",
                "whether justice and law are the same thing"
            ],
            'conflicts': [
                "personal desires versus collective good",
                "tradition against progress",
                "faith versus empirical evidence",
                "duty against personal happiness",
                "survival versus maintaining humanity",
                "individual freedom versus social responsibility",
                "love versus duty",
                "justice versus mercy"
            ],
            'consequences': [
                "forcing everyone to confront their own moral boundaries",
                "revealing the true cost of their principles",
                "challenging everything they believed about right and wrong",
                "showing how good intentions can lead to devastating results",
                "demonstrating how moral choices ripple through generations",
                "proving that the hardest battles are fought within ourselves"
            ]
        }

        templates = {
            Idea.Category.PLOT: [
                "The protagonist discovers {discovery} which leads to {consequence}",
                "In a twist of fate, {event} causes {result}",
                "What starts as {discovery} escalates into {result}",
                "The {event} forces everyone to deal with {consequence}",
            ],
            Idea.Category.CHARACTER: [
                "A mysterious figure who {trait} and harbors {secret}",
                "Someone known for {characteristic} but struggling with {flaw}",
                "A character whose {trait} becomes crucial when {secret} is revealed",
                "An enigmatic person combining {characteristic} with {flaw}",
            ],
            Idea.Category.SETTING: [
                "A world where {condition} and {feature} is commonplace",
                "In {location}, {atmosphere} creates unique challenges",
                "A realm defined by {condition}, where {feature} shapes society",
                "{location} exists in a state of {atmosphere}",
            ],
            Idea.Category.THEME: [
                "Exploring {moral_question} when characters face {conflict}",
                "The story examines {moral_question}, ultimately {consequence}",
                "A tale about {conflict}, asking whether {moral_question}",
                "When {conflict} leads to {consequence}, characters must decide {moral_question}"
            ]
        }

        if category not in templates:
            return f"Generic content for {category} category"

        template = random.choice(templates[category])
        elements = {
            'discovery': random.choice(plot_elements['discoveries']),
            'consequence': random.choice(plot_elements['consequences']),
            'event': random.choice(plot_elements['events']),
            'result': random.choice(plot_elements['results']),
            'trait': random.choice(character_elements['traits']),
            'secret': random.choice(character_elements['secrets']),
            'characteristic': random.choice(character_elements['characteristics']),
            'flaw': random.choice(character_elements['flaws']),
            'condition': random.choice(setting_elements['conditions']),
            'feature': random.choice(setting_elements['features']),
            'location': random.choice(setting_elements['locations']),
            'atmosphere': random.choice(setting_elements['atmospheres']),
            'moral_question': random.choice(theme_elements['moral_questions']),
            'conflict': random.choice(theme_elements['conflicts']),
            'consequence': random.choice(theme_elements['consequences'])
        }

        return template.format(**elements)

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Date range for random timestamps (last 6 months)
        end_date = timezone.now()
        start_date = end_date - timedelta(days=180)

        projects = []
        project_data = [
            ('The Dragon\'s Tale', Project.Genre.FANTASY, Project.Genre.ROMANCE),
            ('Murder in the walled city', Project.Genre.MISTERY, Project.Genre.DRAMA),
            ('The last colony', Project.Genre.SCIFI, Project.Genre.DETECTIVE),
            ('Shadows of Yesterday', Project.Genre.HORROR, Project.Genre.DRAMA),
            ('Growing Pains', Project.Genre.AGE, Project.Genre.COMEDY),
            ('The Laughing Detective', Project.Genre.DETECTIVE, Project.Genre.COMEDY),
            ('Star Knights', Project.Genre.SCIFI, Project.Genre.FANTASY),
        ]

        for name, main_genre, mix_genre in project_data:
            project = Project.objects.create(
                name=name,
                main_genre=main_genre,
                mix_genre=mix_genre,
                created_at=self.generate_random_date(start_date, end_date)
            )
            projects.append(project)
            self.stdout.write(f'Created project: {name}')

        for project in projects:
            for _ in range(10):
                category = random.choice(list(Idea.Category))
                content = self.generate_content(category)
                created_at = self.generate_random_date(project.created_at, end_date)

                idea = Idea.objects.create(
                    content=content,
                    category=category,
                    project=project,
                    created_at=created_at,
                    updated_at=created_at,
                    title=content[:50] + "..." if len(content) > 50 else content
                )

                Idea.objects.filter(pk=idea.pk).update(
                    search_vector=SearchVector('content')
                )

                self.stdout.write(f'Created idea for project: {project.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated test database'))