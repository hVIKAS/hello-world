# Generated by Django 2.0.6 on 2018-07-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddb',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
