# Generated by Django 2.0 on 2019-04-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_auto_20190419_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Male', 'Female')], max_length=10),
        ),
    ]