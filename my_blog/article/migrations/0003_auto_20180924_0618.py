# Generated by Django 2.1 on 2018-09-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20180924_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]