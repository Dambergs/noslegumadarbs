# Generated by Django 3.2.2 on 2021-05-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.DecimalField(decimal_places=6, max_digits=18)),
                ('term', models.DecimalField(decimal_places=2, max_digits=2)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('interest', models.DecimalField(decimal_places=6, max_digits=18)),
            ],
        ),
    ]
