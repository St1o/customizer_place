# Generated by Django 4.0.3 on 2022-04-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioninfo',
            name='cover',
            field=models.FileField(blank=True, upload_to='collection/images/'),
        ),
    ]
