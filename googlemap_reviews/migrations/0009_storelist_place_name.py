# Generated by Django 5.0.2 on 2024-05-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlemap_reviews', '0008_alter_keywordreviews_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='storelist',
            name='place_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
