# Generated by Django 3.0.4 on 2020-06-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0005_auto_20200625_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]