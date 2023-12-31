# Generated by Django 4.2.5 on 2023-09-08 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destroyed_by', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=300)),
                ('path', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
    ]
