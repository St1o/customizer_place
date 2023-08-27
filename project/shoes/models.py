from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings

from owner.models import Owner


class ShoesInfo(models.Model):
    name = models.CharField(verbose_name='shoes name', max_length=255, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)  # disponible par defaut
    price = models.CharField(verbose_name='price', max_length=255)
    cover = models.FileField(upload_to='shoes/images/', blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='owner', default=Owner.get_default_pk,
                              related_name='owner_shoes')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'INFO '
        verbose_name_plural = 'INFOS'
        ordering = ['-created_at']


class ShoesPhoto(models.Model):
    photo = models.ImageField(verbose_name='Photos', upload_to='shoes/images/', blank=False, null=False)
    detail = models.ForeignKey(ShoesInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.detail.name}"

    def get_photo(self):
        if not self.photo:
            return str(settings.MEDIA_ROOT) + 'shoes/images/macula.jpg'  # по умолчанию
        return self.photo.url

    # for create a fictive bd to save img
    def photo_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.get_photo())

    photo_tag.short_description = 'Photo'

    class Meta:
        verbose_name = 'SHOES PHOTO '
        verbose_name_plural = ' PHOTOS'

