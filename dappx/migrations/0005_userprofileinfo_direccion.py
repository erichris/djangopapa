# Generated by Django 2.1.2 on 2018-10-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0004_auto_20181023_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='direccion',
            field=models.CharField(default='', max_length=30),
        ),
    ]
