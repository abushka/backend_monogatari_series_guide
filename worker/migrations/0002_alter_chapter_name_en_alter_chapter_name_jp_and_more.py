# Generated by Django 4.1.5 on 2023-06-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (английский)'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (японский)'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (русский)'),
        ),
        migrations.AlterField(
            model_name='season',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (английский)'),
        ),
        migrations.AlterField(
            model_name='season',
            name='name_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (японский)'),
        ),
        migrations.AlterField(
            model_name='season',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (русский)'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (английский)'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (японский)'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (русский)'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (английский)'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name_jp',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (японский)'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название (русский)'),
        ),
    ]