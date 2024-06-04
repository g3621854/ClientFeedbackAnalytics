# Generated by Django 5.0.2 on 2024-05-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemap_reviews', '0005_rename_store_keywordreviews_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordreviews',
            name='category',
            field=models.BooleanField(choices=[(True, '好評'), (False, '負評')], verbose_name='類別'),
        ),
    ]
