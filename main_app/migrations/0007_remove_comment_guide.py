# Generated by Django 4.2.7 on 2023-11-30 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='guide',
        ),
    ]
