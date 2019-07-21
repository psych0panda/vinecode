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
    slug = models.SlugField(max_length=150, unique_for_date='date_create', default='')
    date = models.DateField()
    wine = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    variety = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    vintage = models.DateField()
    alcohol = models.FloatField()
    price = models.PositiveSmallIntegerField()
    appearance = models.CharField(max_length=150)
    aromas = models.CharField(max_length=150)
    flavors = models.CharField(max_length=150)
    score = models.SmallIntegerField(choices=SCORE_CHOICES)

    class Meta:
        ordering = ('-date_create',)

    def __str__(self):
        return self.wine
