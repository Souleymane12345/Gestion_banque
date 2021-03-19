# Generated by Django 3.1.6 on 2021-02-20 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donnecommune',
            name='identifiant',
        ),
        migrations.AddField(
            model_name='agent',
            name='identifiant',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banque',
            name='identifiant',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='identifiant',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
