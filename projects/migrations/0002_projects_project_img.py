# Generated by Django 5.0 on 2024-02-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
