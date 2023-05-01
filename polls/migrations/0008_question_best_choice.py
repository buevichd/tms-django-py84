# Generated by Django 4.1.7 on 2023-04-26 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='best_choice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='best_question', to='polls.choice'),
        ),
    ]
