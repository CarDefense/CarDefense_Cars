# Generated by Django 2.1.2 on 2018-11-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
