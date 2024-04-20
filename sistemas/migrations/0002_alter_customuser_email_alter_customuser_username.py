# Generated by Django 5.0.4 on 2024-04-18 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Usuario'),
        ),
    ]
