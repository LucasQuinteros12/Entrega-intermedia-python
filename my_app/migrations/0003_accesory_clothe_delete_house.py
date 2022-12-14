# Generated by Django 4.1.2 on 2022-11-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clothe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('size', models.IntegerField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='House',
        ),
    ]
