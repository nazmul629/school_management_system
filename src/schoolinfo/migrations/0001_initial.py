# Generated by Django 2.0 on 2019-04-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schoolinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=100, unique=True)),
                ('school_img', models.ImageField(upload_to='')),
                ('school_address', models.TextField()),
            ],
        ),
    ]
