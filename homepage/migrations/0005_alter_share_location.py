# Generated by Django 4.0.2 on 2022-07-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_share_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='Location',
            field=models.TextField(),
        ),
    ]