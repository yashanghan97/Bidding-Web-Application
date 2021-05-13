# Generated by Django 3.0.8 on 2020-10-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('seller', models.CharField(max_length=64)),
                ('item_id', models.IntegerField()),
                ('final_price', models.IntegerField()),
            ],
        ),
    ]
