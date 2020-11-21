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
    description = models.TextField(verbose_name='Mô tả',blank=True)
    type_vehicle=models.CharField(max_length=50,verbose_name='Loại xe')
    color=models.CharField(max_length=30,verbose_name='Màu sắc',default='')
    cc=models.FloatField(verbose_name='Phân khối')
    price = models.DecimalField(max_digits=10,decimal_places=1,verbose_name='Giá')
    category = models.ForeignKey(Category, verbose_name='Nhóm', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Ảnh', upload_to='static/images')
    year=models.CharField(max_length=10,verbose_name='Năm sản xuất')
    origin=models.CharField(max_length=100,verbose_name='Xuất xứ')
    def __str__(self):
        return self.name
    
class Order(models.Model):
    class Status:
        NEW=0
        DELIVERD=1
        CANCELED=2
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    qty=models.IntegerField(verbose_name='Số lượng')
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=20)
    customer_address=models.CharField(max_length=200)
    order_date=models.DateTimeField()
    deliver_date=models.DateTimeField(null=True)
    status=models.IntegerField()