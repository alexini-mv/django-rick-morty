# Generated by Django 4.0.4 on 2022-05-20 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opcion',
            old_name='pregunta_id',
            new_name='pregunta',
        ),
    ]