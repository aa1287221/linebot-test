# Generated by Django 2.1.5 on 2019-08-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20190822_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
