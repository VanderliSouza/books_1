# Generated by Django 2.0 on 2018-02-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
