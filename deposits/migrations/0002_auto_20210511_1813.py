# Generated by Django 3.2.2 on 2021-05-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='deposit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='interest',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='term',
            field=models.FloatField(),
        ),
    ]
