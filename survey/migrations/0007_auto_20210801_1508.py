# Generated by Django 2.2 on 2021-08-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20210801_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyform',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
