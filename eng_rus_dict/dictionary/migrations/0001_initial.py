# Generated by Django 4.2.5 on 2023-10-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EngRusWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng', models.CharField(max_length=1000)),
                ('rus', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
    ]
