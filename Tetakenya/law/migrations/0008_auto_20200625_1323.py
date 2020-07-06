# Generated by Django 3.0.4 on 2020-06-25 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0007_client_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='law.Lawyer'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='law.Lawyer')),
            ],
        ),
    ]