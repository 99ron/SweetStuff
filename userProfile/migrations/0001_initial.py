# Generated by Django 3.1.2 on 2020-10-29 18:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='users', serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=12, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numbers are allowed.')], verbose_name='Phone Number')),
                ('street_address1', models.CharField(max_length=40, verbose_name='First line of Address')),
                ('street_address2', models.CharField(blank=True, max_length=40, verbose_name='Second line of Address')),
                ('postcode', models.CharField(max_length=50, verbose_name='Postcode')),
                ('town_city', models.CharField(max_length=40, verbose_name='Town/City')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('employee', models.BooleanField(default=False)),
            ],
        ),
    ]