# Generated by Django 3.1.4 on 2021-07-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0004_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialize',
            name='group_name',
            field=models.CharField(default=1, max_length=290),
            preserve_default=False,
        ),
    ]
