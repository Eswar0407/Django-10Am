# Generated by Django 3.2.3 on 2021-08-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='my_Documents/')),
            ],
        ),
    ]