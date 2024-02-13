from django.db import models
from django.core.exceptions import ValidationError

class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title

    def clean(self):
        if not self.title:
            raise ValidationError({'title': 'Заголовок задания должен быть заполнен'})
        super().clean()
