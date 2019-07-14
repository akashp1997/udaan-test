# Generated by Django 2.2.2 on 2019-07-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='assetname',
            field=models.CharField(max_length=255, verbose_name='Asset Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_of_allocation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to_be_performed_by',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
