# Generated by Django 4.0.4 on 2022-05-31 13:56

from django.db import migrations, models
import plate.validators


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0002_user_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('store_name', models.CharField(max_length=20)),
                ('store_link', models.URLField(validators=[plate.validators.validate_store_link])),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('image_1', models.ImageField(upload_to='review_pics')),
                ('image_2', models.ImageField(blank=True, upload_to='review_pics')),
                ('image_3', models.ImageField(blank=True, upload_to='review_pics')),
                ('content', models.TextField()),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임 입니다'}, max_length=15, null=True, unique=True, validators=[plate.validators.validate_no_special_characters]),
        ),
    ]
