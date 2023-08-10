from django.db import models

# Create your models here.
class Application(models.Model):
    name=models.CharField('Имя', max_length=20)
    phone_number=models.CharField('Номер телефона', max_length=20)
    product=models.TextField('Металл в наличии', )

    def __str__(self):
        return self.name + ' ' + self.phone_number

    class Meta:
        verbose_name="Заявка"
        verbose_name_plural = "Заявки"

class Prices(models.Model):
    metal=models.CharField('Металл', max_length=20)
    price=models.FloatField('Цена')

    def __str__(self):
        return self.metal

    class Meta:
        verbose_name="Цена"
        verbose_name_plural = "Цены"