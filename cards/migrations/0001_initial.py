# Generated by Django 4.1.3 on 2022-12-08 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suit', models.PositiveSmallIntegerField(choices=[(3, 'SPADES'), (0, 'CLUBS'), (1, 'DIAMONDS'), (2, 'HEARTS')])),
                ('rank', models.CharField(max_length=5)),
                ('image', models.ImageField(blank=True, default='B-Red.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('coin', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, default='car.png', null=True, upload_to='')),
            ],
        ),
    ]
