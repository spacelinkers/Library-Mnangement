# Generated by Django 2.1.4 on 2018-12-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='image',
        ),
    ]
