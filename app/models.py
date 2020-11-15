from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=30, verbose_name='Mã', unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=30,verbose_name='Mã',  unique=True)
    name = models.CharField(max_length=200, verbose_name='Tên')
    description = models.CharField(max_length=500, verbose_name='Mô tả',  blank=True)
    price = models.FloatField(verbose_name='Giá')
    category = models.ForeignKey(Category, verbose_name='Nhóm', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Ảnh', upload_to='static/images')
    year=models.CharField(max_length=10,verbose_name='Năm sản xuất')
    origin=models.CharField(max_length=100,verbose_name='Xuất xứ')
    def __str__(self):
        return self.name