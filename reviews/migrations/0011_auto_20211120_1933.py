# Generated by Django 2.2.16 on 2021-11-20 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20211120_0349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='genretitle',
            options={},
        ),
    ]
