# Generated by Django 5.1.1 on 2024-09-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimientos',
            field=models.DateField(null=True),
        ),
    ]
