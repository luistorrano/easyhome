# Generated by Django 2.1.1 on 2018-10-17 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20181016_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='republica',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
