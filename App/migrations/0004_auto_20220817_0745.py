# Generated by Django 3.2 on 2022-08-17 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20220817_0729'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='action',
            table='cnext_taskman_action',
        ),
        migrations.AlterModelTable(
            name='taskman',
            table='cnext_taskman',
        ),
    ]
