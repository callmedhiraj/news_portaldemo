# Generated by Django 3.0.4 on 2020-05-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsportal', '0003_auto_20200326_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='menu_display',
            field=models.BooleanField(default=True),
        ),
    ]
