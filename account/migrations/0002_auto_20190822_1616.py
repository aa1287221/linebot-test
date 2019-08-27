# Generated by Django 2.1.5 on 2019-08-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('realname', models.CharField(max_length=4)),
                ('useremail', models.EmailField(max_length=254)),
                ('password', models.SlugField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
