from django.db import models


# Create your models here.
class Worker(models.Model):
    CHOISES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    )
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=2, choices=CHOISES, verbose_name='Пол')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='Отдел')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название отдела')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг')
    floor = models.IntegerField(verbose_name='Этаж')

    @property
    def worker(self):
        return Worker.objects.filter(department__id=self.pk).count()

    def __str__(self):
        return f'{self.name} ({self.floor} этаж)'


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название языка')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')

    @property
    def worker(self):
        return Worker.objects.filter(language__id=self.pk).count()

    def __str__(self):
        return f'{self.name}'
