# Generated by Django 3.1.2 on 2020-10-17 16:10

from django.db import migrations, models
import forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20201017_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=forum.models.saveimage),
        ),
    ]