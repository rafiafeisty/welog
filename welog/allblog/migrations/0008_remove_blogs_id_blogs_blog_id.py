# Generated by Django 5.0.3 on 2025-06-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allblog', '0007_alter_blogs_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='id',
        ),
        migrations.AddField(
            model_name='blogs',
            name='blog_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
