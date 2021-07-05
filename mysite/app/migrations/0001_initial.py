# Generated by Django 3.2.5 on 2021-07-04 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=9, unique=True, verbose_name='rut')),
                ('fono', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=9, unique=True, verbose_name='rut')),
                ('fono', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_servicio', models.CharField(max_length=6)),
                ('nombre_servicio', models.CharField(max_length=20)),
                ('puntos_servicio', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_de_pago', models.CharField(max_length=10)),
                ('Servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cita')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_servicio_empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.empleado')),
                ('Servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cita')),
                ('Servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_puntos_cliente', models.CharField(max_length=2)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('Servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.empleado'),
        ),
        migrations.AddField(
            model_name='cita',
            name='nombre_servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_servicio'),
        ),
    ]
