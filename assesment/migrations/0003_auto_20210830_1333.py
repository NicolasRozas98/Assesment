# Generated by Django 2.2.24 on 2021-08-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assesment', '0002_auto_20210825_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datacollected',
            old_name='type',
            new_name='type_choice',
        ),
        migrations.AlterField(
            model_name='datacollected',
            name='location',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
