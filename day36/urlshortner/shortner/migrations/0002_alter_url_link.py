# Generated by Django 4.1.3 on 2023-11-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='link',
            field=models.CharField(max_length=10000),
        ),
    ]
