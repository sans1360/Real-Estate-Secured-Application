# Generated by Django 4.1.7 on 2023-03-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyDescription', models.CharField(max_length=500)),
                ('propertyArea', models.CharField(max_length=20)),
                ('propertyBeds', models.IntegerField(max_length=10)),
                ('propertyBaths', models.IntegerField(max_length=10)),
                ('propertyGarages', models.IntegerField(max_length=10)),
                ('propertyPrice', models.IntegerField(max_length=10)),
                ('propertyLocation', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=10)),
                ('contactDetails', models.IntegerField(max_length=20)),
                ('bhkType', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
