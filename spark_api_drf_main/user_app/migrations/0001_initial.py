# Generated by Django 4.0.6 on 2022-07-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('dateMiseAJour', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
