from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    date_of_completion = models.DateTimeField(blank=True,
                                              null=True)
    completed = models.BooleanField(default=False)

    def is_expired(self):
        from django.utils import timezone
        if self.date_of_completion:
            return self.date_of_completion < timezone.now()

    @property
    def completed_text(self):
        return 'completed' if self.completed else 'not completed'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        ordering = ['date_of_completion']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Tag(models.Model):
    name = models.CharField(max_length=64)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
