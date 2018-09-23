# Generated by Django 2.1.1 on 2018-09-23 07:58

from django.db import migrations, models
import livegene.apps.livegene.validators


class Migration(migrations.Migration):

    dependencies = [
        ('livegene', '0003_auto_20180921_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default='', max_length=8, unique=True, validators=[livegene.apps.livegene.validators.validate_lowercase]),
            preserve_default=False,
        ),
    ]
