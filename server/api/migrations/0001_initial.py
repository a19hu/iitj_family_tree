# Generated by Django 3.2.12 on 2024-06-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=9, unique=True)),
                ('year', models.CharField(max_length=4)),
                ('picture', models.URLField(blank=True, null=True)),
                ('parentId', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('linkedIn', models.URLField(blank=True, null=True)),
            ],
        ),
    ]