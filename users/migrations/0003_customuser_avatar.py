# Generated by Django 4.1 on 2022-09-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_bio_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
