# Generated by Django 2.2.6 on 2020-01-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.SmallIntegerField()),
                ('info', models.TextField()),
            ],
        ),
    ]
