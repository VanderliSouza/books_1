# Generated by Django 2.0 on 2018-03-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180302_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='covers/%Y,%m/,%d/'),
        ),
    ]
