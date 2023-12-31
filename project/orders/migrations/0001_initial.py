# Generated by Django 3.2.9 on 2022-12-10 14:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0002_alter_collectioninfo_cover'),
        ('shoes', '0005_alter_shoesinfo_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('articles_name', models.CharField(max_length=255, verbose_name='articles name')),
                ('articles_price', models.CharField(max_length=255, verbose_name='articles price')),
                ('articles_photo', models.ImageField(upload_to='orders/images/', verbose_name='articles photos')),
                ('name', models.CharField(max_length=255, verbose_name='client name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date of creation order')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date of modification order')),
            ],
            options={
                'verbose_name': 'Order ',
                'verbose_name_plural': 'Orders',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collections', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.collectioninfo')),
                ('shoes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoes.shoesinfo')),
            ],
            options={
                'verbose_name': 'Article ',
                'verbose_name_plural': 'Articles',
                'ordering': ['-id'],
            },
        ),
    ]
