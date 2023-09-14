# Generated by Django 3.2.10 on 2023-07-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointmntdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('Doctors', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('phonenum', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
