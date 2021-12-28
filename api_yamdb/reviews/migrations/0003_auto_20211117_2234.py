# Generated by Django 2.2.16 on 2021-11-17 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211117_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.TextField(max_length=256),
        ),
    ]
