# Generated by Django 3.2.6 on 2021-08-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20210810_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
    ]
