# Generated by Django 5.1.1 on 2024-10-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideasrecording', '0004_alter_project_mix_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_genre',
            field=models.CharField(choices=[('ROMANCE', 'romance'), ('MISTERY', 'mistery'), ('SCI-FI', 'sci-fi'), ('FANTASY', 'fantasy'), ('ACTION', 'action'), ('DRAMA', 'drama'), ('DETECTIVE', 'detective'), ('HORROR', 'horror'), ('COMING OF AGE', 'coming of age'), ('COMEDY', 'comedy'), ('NONE', 'none')], max_length=13),
        ),
        migrations.AlterField(
            model_name='project',
            name='mix_genre',
            field=models.CharField(blank=True, choices=[('ROMANCE', 'romance'), ('MISTERY', 'mistery'), ('SCI-FI', 'sci-fi'), ('FANTASY', 'fantasy'), ('ACTION', 'action'), ('DRAMA', 'drama'), ('DETECTIVE', 'detective'), ('HORROR', 'horror'), ('COMING OF AGE', 'coming of age'), ('COMEDY', 'comedy'), ('NONE', 'none')], max_length=13),
        ),
    ]
