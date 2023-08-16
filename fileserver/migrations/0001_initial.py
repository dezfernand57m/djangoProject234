# Generated by Django 4.2.4 on 2023-08-16 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('unit', models.CharField(max_length=12)),
                ('personal_code', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Fileu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datepublish', models.DateField()),
                ('filz', models.FileField(upload_to='upload/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileserver.user')),
            ],
        ),
    ]
