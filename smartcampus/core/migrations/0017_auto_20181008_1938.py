# Generated by Django 2.1.2 on 2018-10-08 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20181006_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleboardcomputer',
            name='single_board_computer_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Singleboardcomputertype'),
        ),
    ]
