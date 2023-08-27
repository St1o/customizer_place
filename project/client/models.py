from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=512, verbose_name='username')
    telephone = models.CharField(max_length=30, verbose_name='tel')
    email = models.EmailField(max_length=200, verbose_name='email')
    is_active = models.BooleanField(verbose_name='actif', default=False)
    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of modification', auto_now=True)

    class Meta:
        verbose_name = 'Client '
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.name

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

