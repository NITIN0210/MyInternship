# Generated by Django 3.2.4 on 2021-06-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
