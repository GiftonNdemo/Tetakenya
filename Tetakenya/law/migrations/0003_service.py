# Generated by Django 3.0.4 on 2020-06-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0002_auto_20200624_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Name', models.CharField(max_length=50)),
                ('Service_Cost', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
