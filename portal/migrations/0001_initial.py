# Generated by Django 3.0.2 on 2020-01-18 17:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('data_ins', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('data_ins', models.DateTimeField(default=django.utils.timezone.now)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Site')),
            ],
        ),
    ]