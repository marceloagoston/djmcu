# Generated by Django 3.0 on 2020-01-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0003_auto_20200123_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenaza',
            name='impacto',
            field=models.IntegerField(choices=[('Bajo', 1), ('Medio', 2), ('Alto', 3)], default=1),
        ),
        migrations.AddField(
            model_name='amenaza',
            name='prob',
            field=models.IntegerField(choices=[('Bajo', 1), ('Medio', 2), ('Alto', 3)], default=1),
        ),
    ]