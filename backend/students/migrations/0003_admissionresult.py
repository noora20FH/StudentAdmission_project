# Generated by Django 4.2.1 on 2023-06-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_registraionno_student_registrationno'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionResult',
            fields=[
                ('studentId', models.AutoField(primary_key=True, serialize=False)),
                ('stdName', models.CharField(max_length=100)),
                ('Result', models.CharField(max_length=100)),
            ],
        ),
    ]