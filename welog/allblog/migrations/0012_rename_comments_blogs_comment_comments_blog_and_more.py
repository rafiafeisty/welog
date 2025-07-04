# Generated by Django 5.0.3 on 2025-06-21 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allblog', '0011_comments_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='allblog.blogs'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
