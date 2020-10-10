# Generated by Django 3.0 on 2020-10-10 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activos', '0016_auto_20200309_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenazas',
            fields=[
                ('id_Amenaza', models.AutoField(primary_key=True, serialize=False)),
                ('amenaza', models.CharField(max_length=100)),
                ('probabilidad', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('impacto', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('anteriorRiesgo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoAmenazas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riesgoAnterior', models.IntegerField(blank=True, null=True)),
                ('id_fk_amenaza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenazas_acttual', to='activos.Amenazas')),
            ],
        ),
        migrations.RemoveField(
            model_name='historicoamenaza',
            name='id_f_amenaza',
        ),
        migrations.RenameModel(
            old_name='Activo',
            new_name='Activos',
        ),
        migrations.DeleteModel(
            name='Amenaza',
        ),
        migrations.DeleteModel(
            name='HistoricoAmenaza',
        ),
        migrations.AddField(
            model_name='amenazas',
            name='activo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenazas_activo', to='activos.Activos'),
        ),
    ]
