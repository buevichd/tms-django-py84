# Generated by Django 4.1.7 on 2023-04-26 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question_best_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='best_choice',
        ),
    ]
