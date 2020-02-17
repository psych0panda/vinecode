from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Note(models.Model):
    PERFECTLY = 5
    GOOD = 4
    SATISFACTORILY = 3
    BAD = 2
    ABOMINATION = 1
    SCORE_CHOICES = (
        (5, 'Отлично'),
        (4, 'Хорошо'),
        (3, 'Удовлетворительно'),
        (2, 'Плохо'),
        (1, 'Уксус'),
    )
    date_create = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notes')
    slug = models.SlugField(max_length=150, unique_for_date='date_create', default="")
    date = models.DateField(verbose_name="Дата дегустации")
    wine = models.CharField(max_length=150, verbose_name="Название")
    region = models.CharField(max_length=150, verbose_name="Регион")
    variety = models.CharField(max_length=150, verbose_name="Сорт")
    country = models.CharField(max_length=150, verbose_name="Страна происхождения")
    vintage = models.DateField(verbose_name="Год урожая")
    alcohol = models.FloatField(verbose_name="Содержание алкоголя")
    price = models.PositiveSmallIntegerField(verbose_name="Цена")
    appearance = models.CharField(max_length=150, verbose_name="Внешний вид")
    aromas = models.CharField(max_length=300, verbose_name="Аромат")
    flavors = models.CharField(max_length=300, verbose_name="Вкус")
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name="Общая оценка")

    class Meta:
        ordering = ('-date_create',)

    def __str__(self):
        return self.wine
