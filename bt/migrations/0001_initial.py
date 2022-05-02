# Generated by Django 3.2.2 on 2022-05-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('date_book', models.DateField()),
                ('time', models.DateTimeField()),
                ('people', models.IntegerField(default=1)),
                ('message', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('subject', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
