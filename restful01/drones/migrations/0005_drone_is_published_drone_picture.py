# Generated by Django 5.1 on 2024-11-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0004_drone_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drone',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='drones_images/'),
        ),
    ]
