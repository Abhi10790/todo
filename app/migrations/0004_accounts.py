# Generated by Django 3.2.4 on 2021-06-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210621_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('fullname', models.CharField(max_length=100)),
                ('emailid', models.TextField()),
                ('password', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
