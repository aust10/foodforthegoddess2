# Generated by Django 3.0.2 on 2020-01-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='key_words',
        ),
        migrations.AddField(
            model_name='recipe',
            name='key_words',
            field=models.ManyToManyField(to='recipe_app.KeyWord', verbose_name='KeyWord'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='technique',
        ),
        migrations.AddField(
            model_name='recipe',
            name='technique',
            field=models.ManyToManyField(to='recipe_app.Technique', verbose_name='Technique'),
        ),
    ]
