# Generated by Django 2.2 on 2021-08-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20210731_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('nam', 'Nam'), ('nữ', 'Nữ')], default='Nam', max_length=5)),
                ('age', models.IntegerField(default=18, verbose_name='Nhập tuổi')),
                ('result', models.BooleanField()),
                ('audio_path', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'survey',
            },
        ),
        migrations.DeleteModel(
            name='survey',
        ),
    ]