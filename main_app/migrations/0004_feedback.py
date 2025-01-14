# Generated by Django 5.1.2 on 2024-11-05 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_receiver_request_donor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('Replay', models.CharField(blank=True, max_length=200, null=True)),
                ('Receiver_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.receiver')),
            ],
        ),
    ]
