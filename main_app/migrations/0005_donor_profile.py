# Generated by Django 5.1.2 on 2024-11-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='profile',
            field=models.FileField(default=1, upload_to='profile/'),
            preserve_default=False,
        ),
    ]
