# Generated by Django 3.2.9 on 2021-11-30 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название отдела')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Слаг')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название языка')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('sex', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=2, verbose_name='Пол')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.department', verbose_name='Отдел')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language', verbose_name='Язык')),
            ],
        ),
    ]
