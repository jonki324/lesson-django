from django.db import models

class Publisher(models.Model):
    name = models.CharField(verbose_name='出版社', max_length=255)

class Author(models.Model):
    name = models.CharField(verbose_name='著作者', max_length=255)

class Book(models.Model):
    class Meta:
        db_table = 'books'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, verbose_name='著者')

    def __str__(self):
        return self.title

class BookStock(models.Model):
    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)
