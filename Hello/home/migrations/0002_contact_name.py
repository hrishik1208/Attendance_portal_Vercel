# Generated by Django 4.0.4 on 2022-05-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='kshh', max_length=100),
        ),
    ]
