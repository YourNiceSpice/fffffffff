# Generated by Django 4.0.3 on 2022-03-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0005_remove_room_member_count_remove_room_token_haveachat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
