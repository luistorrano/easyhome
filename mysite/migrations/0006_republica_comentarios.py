# Generated by Django 2.1.1 on 2018-09-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_usuario_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='republica',
            name='comentarios',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
