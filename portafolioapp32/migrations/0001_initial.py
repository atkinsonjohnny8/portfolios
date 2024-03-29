# Generated by Django 3.2 on 2023-12-13 01:25

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('rol', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Contractor'), (2, 'Developer')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=255)),
                ('projectfile', models.FileField(upload_to='projectuploads/')),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolioapp32.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('remote_work', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Yes'), (2, 'No')], null=True)),
                ('salary', models.IntegerField(blank=True, choices=[(100, '100-200'), (200, '200-400'), (400, '400-1000'), (1000, '1000-1200')], null=True)),
                ('cv', models.FileField(upload_to='uploads/')),
                ('nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolioapp32.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=255)),
                ('messagetitle', models.CharField(max_length=255)),
                ('messagebody', models.CharField(max_length=255)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolioapp32.usuario')),
            ],
        ),
    ]
