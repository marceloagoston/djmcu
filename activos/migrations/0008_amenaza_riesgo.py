# Generated by Django 3.0 on 2020-01-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0007_auto_20200123_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenaza',
            name='riesgo',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]
