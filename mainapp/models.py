from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField('Название', max_length=150)
    img = models.ImageField('Картинка', upload_to='ducks/')
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена', help_text='Указывать сумму в рублях.')
    for_sale = models.BooleanField('Продается', default=False)
    safe_sale = models.BooleanField('Безопасная сделка', default=False)
    delivery = models.BooleanField('Возможна доставка', default=False)
    address = models.CharField('Адрес', max_length=250)
    seller = models.CharField('Продавец', max_length=150)
    phone = models.CharField('Телефон', max_length=15)
    pin_code = models.PositiveSmallIntegerField('Пин код')
    added = models.TimeField('Добавлено', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-added']

    def get_absolute_url(self):
        return reverse('detail_item_url', kwargs={'pk': self.id})
