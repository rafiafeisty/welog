# Generated by Django 5.0.3 on 2025-06-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
