# Generated by Django 4.1.7 on 2023-07-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolldata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('btime', models.CharField(max_length=50)),
                ('pay_mode', models.CharField(max_length=50)),
                ('name_on_card', models.CharField(max_length=50)),
                ('card_no', models.CharField(max_length=50)),
                ('expiry', models.CharField(max_length=50)),
                ('cvv', models.CharField(max_length=50)),
            ],
        ),
    ]