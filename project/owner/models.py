from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Shop name', unique=True)
    address = models.CharField(max_length=255, verbose_name='address')

    @classmethod
    def get_default_pk(cls):
        shop, created = cls.objects.get_or_create(
            name='admin', defaults=dict(address='root'))
        return shop

    class Meta:
        verbose_name = 'Shop '
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=512, verbose_name='username')
    telephone = models.CharField(max_length=30, verbose_name='tel', unique=True)
    email = models.EmailField(max_length=200, verbose_name='email')
    is_active = models.BooleanField(verbose_name='actif', default=False)
    created_at = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='date of modification', auto_now=True)
    is_owner_shop = models.BooleanField(verbose_name='Store owner', default=True)
    is_superuser = models.BooleanField(verbose_name='admin', default=False)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, verbose_name="shop", primary_key=True)

    @classmethod
    def get_default_pk(cls):
        owner, created = cls.objects.get_or_create(
            name='admin', telephone='+79094307359', is_superuser=True, email='jjjmaxime@gmail.com',
            shop=Shop.get_default_pk())
        return owner.pk

    class Meta:
        verbose_name = 'owner '
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
