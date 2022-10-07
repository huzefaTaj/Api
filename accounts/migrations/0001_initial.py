# Generated by Django 4.1.2 on 2022-10-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('state', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
    ]
