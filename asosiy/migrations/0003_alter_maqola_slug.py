# Generated by Django 4.2.7 on 2023-11-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_maqola_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maqola',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]