# Generated by Django 2.0 on 2017-12-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_meme_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratingReview',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
