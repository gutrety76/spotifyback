# Generated by Django 4.1.5 on 2023-01-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_albums_delete_myplaylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
