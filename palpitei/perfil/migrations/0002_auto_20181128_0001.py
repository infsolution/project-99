# Generated by Django 2.1.3 on 2018-11-28 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='numer',
            new_name='number',
        ),
    ]