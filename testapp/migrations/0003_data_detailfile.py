# Generated by Django 3.2.4 on 2021-06-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_remove_data_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='detailfile',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
