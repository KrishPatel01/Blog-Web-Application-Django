# Generated by Django 3.1.4 on 2021-01-02 13:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_blogpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='BlogComment',
        ),
    ]