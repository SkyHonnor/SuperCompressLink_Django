# Generated by Django 5.0.1 on 2024-01-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectionTable',
            fields=[
                ('coderedirection', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('urlredirection', models.CharField(max_length=2083)),
                ('datecreation', models.DateTimeField(auto_now_add=True)),
                ('datederniereutilisation', models.DateTimeField(null=True)),
            ],
        ),
    ]
