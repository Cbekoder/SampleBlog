# Generated by Django 4.2.7 on 2023-11-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiy', '0004_delete_maqola'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('photo', models.FileField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
