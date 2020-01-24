# Generated by Django 2.2.6 on 2020-01-24 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friends',
            name='last_name',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]