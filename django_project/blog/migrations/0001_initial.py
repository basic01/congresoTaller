# Generated by Django 2.1.5 on 2019-03-10 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taller', models.CharField(max_length=200)),
                ('dia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoPaterno', models.CharField(max_length=100)),
                ('apellidoMaterno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoPaterno', models.CharField(max_length=100)),
                ('apellidoMaterno', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=100)),
                ('institucion', models.CharField(max_length=200)),
                ('mondragon', models.CharField(choices=[('sí', 'Sí'), ('no', 'No')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('actividad', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('ponente', models.CharField(max_length=100)),
                ('cupo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='idParticipante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Participante'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='idTaller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Taller'),
        ),
    ]
