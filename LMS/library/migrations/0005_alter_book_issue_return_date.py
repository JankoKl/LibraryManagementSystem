# Generated by Django 3.2.12 on 2022-09-03 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20220903_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 23, 25, 4, 271802)),
        ),
    ]
