# Generated by Django 3.2.7 on 2022-10-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]