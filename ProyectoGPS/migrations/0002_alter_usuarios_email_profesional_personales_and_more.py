# Generated by Django 4.0.3 on 2022-05-16 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoGPS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGPS.egresados'),
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleo_actual', models.CharField(max_length=50)),
                ('empleo_previo', models.CharField(max_length=50)),
                ('id_em', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGPS.egresados')),
            ],
        ),
        migrations.CreateModel(
            name='Personales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_m', models.CharField(max_length=25)),
                ('apellido_p', models.CharField(max_length=25)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=2, null=True)),
                ('ciudad_radica', models.CharField(blank=True, max_length=25, null=True)),
                ('ciudad_origen', models.CharField(blank=True, max_length=25, null=True)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGPS.egresados')),
            ],
        ),
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Univer', models.CharField(max_length=50)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoGPS.egresados')),
            ],
        ),
    ]
