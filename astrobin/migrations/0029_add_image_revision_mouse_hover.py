# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-10-14 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrobin', '0028_add_image_mouse_hover'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerevision',
            name='mouse_hover_image',
            field=models.CharField(blank=True, default=b'SOLUTION', max_length=16, null=True),
        ),
    ]