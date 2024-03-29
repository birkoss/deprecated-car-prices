# Generated by Django 3.0.6 on 2020-05-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='')),
                ('token', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='')),
                ('year', models.CharField(default='', max_length=4)),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.Make')),
            ],
        ),
        migrations.CreateModel(
            name='Trim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(blank=True, default='', max_length=255)),
                ('nice_name', models.CharField(default='', max_length=255)),
                ('foreign_id', models.CharField(blank=True, default='', max_length=255)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cars.Model')),
            ],
        ),
    ]
