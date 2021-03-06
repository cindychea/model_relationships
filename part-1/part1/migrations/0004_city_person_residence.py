# Generated by Django 2.2.1 on 2019-05-29 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0003_auto_20190529_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('year_founded', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='part1.City')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitants', to='part1.Residence')),
            ],
        ),
    ]
