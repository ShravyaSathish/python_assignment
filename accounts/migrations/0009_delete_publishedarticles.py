# Generated by Django 4.2.3 on 2023-08-04 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PublishedArticles',
        ),
    ]