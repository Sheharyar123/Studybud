# Generated by Django 4.1 on 2022-08-27 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_message_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_on']},
        ),
    ]
