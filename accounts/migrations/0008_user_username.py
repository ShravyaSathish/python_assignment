# Generated by Django 4.2.3 on 2023-08-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_articlesmodel_is_editted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=288),
            preserve_default=False,
        ),
    ]
