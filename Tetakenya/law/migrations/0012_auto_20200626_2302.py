# Generated by Django 3.0.4 on 2020-06-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0011_auto_20200626_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
