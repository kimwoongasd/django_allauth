# Generated by Django 4.0.4 on 2022-05-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
