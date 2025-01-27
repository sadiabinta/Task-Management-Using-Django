# Generated by Django 5.0.7 on 2024-08-18 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('isCompleted', models.BooleanField(default=False)),
                ('assignDate', models.DateField()),
            ],
        ),
    ]
