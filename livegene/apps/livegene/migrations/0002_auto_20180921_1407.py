# Generated by Django 2.1.1 on 2018-09-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livegene', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='logo',
        ),
        migrations.AddField(
            model_name='organisation',
            name='logo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]