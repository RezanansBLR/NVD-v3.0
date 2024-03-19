from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.title


class Account(models.Model):
    offer = models.ForeignKey('Offer', on_delete=models.PROTECT, verbose_name="Оффер")
    post = models.CharField(max_length=50, verbose_name="Почта")
    password = models.CharField(max_length=20, verbose_name="Пароль")
    config_number = models.IntegerField(default=0, verbose_name="Номер конфига")
    creator = models.ForeignKey('Creator', on_delete=models.PROTECT, verbose_name="Создатель")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return str(self.pk)


class Ip(models.Model):
    ip = models.GenericIPAddressField(verbose_name="IP адрес")
    account = models.ForeignKey(Account, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Аккаунт")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="Страна")

    class Meta:
        verbose_name = "IP адрес"
        verbose_name_plural = "IP адреса"

    def __str__(self):
        return self.ip


class Creator(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")

    class Meta:
        verbose_name = "Создатель"
        verbose_name_plural = "Создатели"

    def __str__(self):
        return self.name


class Partner(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    link = models.URLField(verbose_name="Ссылка на ПП")
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='Логин на ПП')
    password = models.CharField(max_length=30,  blank=True, null=True, verbose_name='Пароль на ПП')

    class Meta:
        verbose_name = "Партнерка"
        verbose_name_plural = "Партнерки"

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Страна')
    link = models.CharField(max_length=100, verbose_name="Ссылка для регистрации")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name="Партнерка")

    class Meta:
        verbose_name = "Оффер"
        verbose_name_plural = "Офферы"

    def __str__(self):
        return self.title