# Generated by Django 4.2.5 on 2023-10-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_alter_engrusword_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engrusword',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
