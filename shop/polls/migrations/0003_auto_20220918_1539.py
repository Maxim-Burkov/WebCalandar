# Generated by Django 3.2.15 on 2022-09-18 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_simpleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('is_superuser', models.BooleanField()),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]