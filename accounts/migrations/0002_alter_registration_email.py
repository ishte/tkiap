# Generated by Django 4.0.6 on 2022-07-15 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='email'),
        ),
    ]
