# Generated by Django 4.0.5 on 2022-06-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_api', '0004_alter_music_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]