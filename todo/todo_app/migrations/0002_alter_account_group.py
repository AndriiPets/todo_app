# Generated by Django 3.2.9 on 2022-01-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='accounts', to='todo_app.Group'),
        ),
    ]
