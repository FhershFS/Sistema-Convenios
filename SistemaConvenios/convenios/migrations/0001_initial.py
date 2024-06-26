# Generated by Django 4.1.6 on 2023-11-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaConvenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_salida', models.DateField(blank=True, null=True)),
                ('fecha_termino', models.DateField(blank=True, null=True)),
                ('objeto_convenio', models.CharField(
                    blank=True, max_length=500, null=True)),
                ('tipo_institucion', models.CharField(
                    blank=True, max_length=150, null=True)),
                ('representante_legal', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('recurso_economico', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('PNT', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('PDF_estado', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('visto_bueno', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('documento_editable', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('firmado', models.CharField(blank=True, choices=[
                 ('SI', 'Sí'), ('NO', 'No')], max_length=10, null=True)),
                ('estado', models.CharField(blank=True, choices=[('TERMINADO', 'Terminado'), (
                    'ESPERA', 'En espera'), ('NO EMPEZADO', 'No empezado')], max_length=20, null=True)),
                ('convenio_modificatorio', models.FileField(upload_to='')),
                ('PDF_archivo', models.FileField(upload_to='')),
                ('ubicacion', models.CharField(
                    blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaTramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UnidadAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ConvenioParticipantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('convenio', models.ForeignKey(
                    on_delete=models.SET('N/A'), to='convenios.convenio')),
                ('participante', models.ForeignKey(
                    on_delete=models.SET('N/A'), to='convenios.participantes')),
            ],
        ),
        migrations.AddField(
            model_name='convenio',
            name='participantes',
            field=models.ManyToManyField(to='convenios.participantes'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='persona_tramito',
            field=models.ForeignKey(on_delete=models.SET(
                'N/A'), to='convenios.personatramite'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='tipo',
            field=models.ForeignKey(on_delete=models.SET(
                'N/A'), to='convenios.categoriaconvenio'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='unidad_academica',
            field=models.ForeignKey(on_delete=models.SET(
                'N/A'), to='convenios.unidadacademica'),
        ),
    ]
