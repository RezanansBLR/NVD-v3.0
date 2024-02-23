from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.title
