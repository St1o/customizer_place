from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

from owner.models import Owner


class CollectionInfo(models.Model):
    name = models.CharField(verbose_name='collection name', max_length=255, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)  # disponible par defaut
    price = models.CharField(verbose_name='price', max_length=255)
    cover = models.FileField(upload_to='collection/images/', blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='owner', default=Owner.get_default_pk,
                              related_name='owner_collection')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'INFO '
        verbose_name_plural = 'INFOS'
        ordering = ['-created_at']


class CollectionPhoto(models.Model):
    photo = models.ImageField(verbose_name='Photos', upload_to='collection/images/', blank=False, null=False)
    detail = models.ForeignKey(CollectionInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.detail.name}"

    def get_photo(self):
        if not self.photo:
            return str(settings.MEDIA_ROOT) + 'collection/images/macula.jpg'  # по умолчанию
        return self.photo.url

    # for create a fictive bd to save img
    def photo_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_photo())

    photo_tag.short_description = 'Photo'

    class Meta:
        verbose_name = ' PHOTO '
        verbose_name_plural = 'PHOTOS'


# class Shoes(models.Model):
#     shoes_name =

#
# class CollectionPhoto(models.Model):
#     photo = models.ImageField(verbose_name='Photo', upload_to='collection/images/', blank=False, null=False)
#     name = models.CharField(max_length=255, verbose_name='photo name')
#
#     def __str__(self):
#         return f"{self.photo}"
#
#     def get_photo(self):
#         if not self.photo:
#             return str(settings.MEDIA_ROOT) + 'collection/images/macula.jpg'  # по умолчанию
#         return self.photo.url
#
#     # for create a fictive bd to save img
#     def photo_tag(self):
#         return mark_safe('<img src="%s" width="50" height="50" />' % self.get_photo())
#
#     photo_tag.short_description = 'Photo'
#
#
# class Categories(models.Model):
#     id = models.BigAutoField(verbose_name='id', primary_key=True)
#     name = models.CharField(verbose_name='Shoe name', max_length=255, blank=False)
#     collections_photos = models.ManyToManyField(CollectionPhoto, verbose_name='photo', related_name='collection')
#     description = models.TextField()
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='owner', default=Owner.get_default_pk,
#                               related_name='owner_collection')
#     created_at = models.DateTimeField(auto_now_add=True)
#     available = models.BooleanField(default=True)  # disponible par defaut
#     price = models.CharField(verbose_name='price', max_length=255)
#
#     def __str__(self):
#         return f"{self.collections_photos.all()}"
#
#     def get_photos(self):
#         return [p.photo.url for p in self.collections_photos.all()][0]
#
#     def get_photos_all(self):
#         return [p.photo.url for p in self.collections_photos.all()]
#
#     class Meta:
#         verbose_name = 'COLLECTION CATEGORY '
#         verbose_name_plural = 'COLLECTIONS CATEGORIES'
#         ordering = ['-created_at']
#
# # class Shoes(models.Model):
# #     shoes_name =
