# Generated by Django 3.0.4 on 2020-06-30 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0012_auto_20200626_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='services',
        ),
        migrations.AddField(
            model_name='service',
            name='lawyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='law.Lawyer'),
        ),
    ]