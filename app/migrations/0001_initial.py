# Generated by Django 4.1.7 on 2023-04-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('Topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
