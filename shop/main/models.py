from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    #db_index=True используем к тому что часто используем позволяет например ускорить фильтрацию товаров
    slug = models.SlugField(max_length=100, unique=True)
    # slug нужен для генерации юрлэок на наш продукт

    class Meta: 
        # class Meta параметры с которыми будет работать админка и бд
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    # метод который определяет как будет отображаться обьект в админке


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    #ForeignKey - необходим для наследования, мы в эти категории засунеули модель категории и теперь category имеет все тоже что моделоь категории имя и так далее, related_name='products' - как мы хотим видеть в админке,  on_delete=models.CASCADE - если удалим категорию например смартфоны и удалим тогда 30 наших смартфонов
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # для работы с нецелыми числами, decimal_places сколько цмифр после запятой
    avilable = models.BooleanField(default=True)
    # доступность товара либо есть либо нет
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
