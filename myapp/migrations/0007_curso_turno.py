# Generated by Django 3.1.3 on 2020-12-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_curso_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Noche')], null=True, verbose_name='Turno'),
        ),
    ]
