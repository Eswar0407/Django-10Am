# Generated by Django 3.2.3 on 2021-08-31 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('account_no', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_db.employeemodel')),
            ],
        ),
    ]
