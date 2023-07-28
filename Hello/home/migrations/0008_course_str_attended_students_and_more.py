# Generated by Django 4.0.4 on 2022-05-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_course_str_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_str',
            name='attended_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course_str',
            name='total_registered_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course_str',
            name='date',
            field=models.DateField(default='2021-10-10'),
        ),
    ]
