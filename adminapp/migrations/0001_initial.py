# Generated by Django 3.2.10 on 2023-07-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospitaldb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalname', models.CharField(blank=True, max_length=100, null=True)),
                ('hospitalcode', models.CharField(blank=True, max_length=100, null=True)),
                ('contactno', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address1', models.CharField(blank=True, max_length=500, null=True)),
                ('addrress2', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
