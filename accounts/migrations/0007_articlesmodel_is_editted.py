# Generated by Django 4.2.3 on 2023-08-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_articlesmodel_publisher_publishedarticles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesmodel',
            name='is_editted',
            field=models.BooleanField(default=False),
        ),
    ]
