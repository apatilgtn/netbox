# Generated by Django 2.0.8 on 2018-08-22 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0063_device_local_context_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='rpc_client',
        ),
    ]
