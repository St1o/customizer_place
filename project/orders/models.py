import uuid

from collection.models import *

from shoes.models import *


class Articles(models.Model):
    shoes = models.ForeignKey(ShoesInfo, on_delete=models.SET_NULL, blank=True, null=True)
    collections = models.ForeignKey(CollectionInfo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Article '
        verbose_name_plural = 'Articles'
        ordering = ['-id']


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    articles_name = models.CharField(verbose_name='articles name', max_length=255, blank=False)
    articles_price = models.CharField(verbose_name='articles price', max_length=255, blank=False)
    articles_photo = models.ImageField(verbose_name='articles photos', upload_to='orders/images/', blank=False, null=False)
    name = models.CharField(verbose_name='client name', max_length=255, blank=False)
    created_at = models.DateTimeField(verbose_name='date of creation order', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of modification order', auto_now=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Order '
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']


class Commandes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.CharField(verbose_name="Total", max_length=100,blank=False)
    products = models.JSONField(verbose_name='List Articles (JSON)', null=True, blank=True)
    name = models.CharField(verbose_name='client name', max_length=255, blank=False)
