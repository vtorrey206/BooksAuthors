# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-16 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_remove_book_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Book about a programming language'),
            preserve_default=False,
        ),
    ]
