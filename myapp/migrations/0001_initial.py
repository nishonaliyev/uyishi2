# Generated by Django 4.2.7 on 2023-11-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('sana', models.DateField(blank=True)),
            ],
        ),
    ]