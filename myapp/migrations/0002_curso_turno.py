# Generated by Django 3.1.3 on 2020-12-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Mañana'), (2, 'Tarde'), (3, 'Noche')], null=True),
        ),
    ]
