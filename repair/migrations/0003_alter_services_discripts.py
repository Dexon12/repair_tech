# Generated by Django 4.2.4 on 2023-08-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0002_services_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='discripts',
            field=models.CharField(blank=True, max_length=1800, null=True),
        ),
    ]
