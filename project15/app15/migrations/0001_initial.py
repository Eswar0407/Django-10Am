# Generated by Django 3.2.3 on 2021-07-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('course_no', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
                ('course_fee', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('student_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('course', models.ManyToManyField(to='app15.courseModel')),
            ],
        ),
    ]
