# Generated by Django 3.2.3 on 2021-08-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployyeModel',
            fields=[
                ('Idno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Salary', models.FloatField(max_length=20)),
            ],
        ),
    ]
