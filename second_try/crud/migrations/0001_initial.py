# Generated by Django 2.2.5 on 2020-01-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('edateofbirth', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
