# Generated by Django 3.2.3 on 2021-05-17 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]