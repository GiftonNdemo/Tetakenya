# Generated by Django 3.0.4 on 2020-06-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0006_lawyer_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]