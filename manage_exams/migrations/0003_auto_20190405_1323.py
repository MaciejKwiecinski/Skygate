# Generated by Django 2.1.7 on 2019-04-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_exams', '0002_auto_20190404_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='url',
            field=models.CharField(default='127.0.0.1:8000/api-exam/<built-in function id>', max_length=255),
        ),
        migrations.AddField(
            model_name='exercise',
            name='url',
            field=models.CharField(default='127.0.0.1:8000/api-exercises/<built-in function id>', max_length=255),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.IntegerField(choices=[(1, 'english'), (2, 'PE'), (4, 'informatics'), (0, 'polish'), (3, 'math')]),
        ),
    ]
