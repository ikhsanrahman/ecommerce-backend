# Generated by Django 2.1.5 on 2019-02-22 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20190219_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Subscriber', 'verbose_name_plural': 'Subscribers'},
        ),
    ]