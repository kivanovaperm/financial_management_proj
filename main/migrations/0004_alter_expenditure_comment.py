# Generated by Django 3.2.18 on 2024-01-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20240106_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
    ]
