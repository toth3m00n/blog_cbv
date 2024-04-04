from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.services.utils import unique_slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='profile')
    slug = models.SlugField(max_length=255, verbose_name='URL', blank=True)
    avatar = models.ImageField(
        upload_to='images/avatars/%Y/%m',
        default='images/avatars/default.png',
        verbose_name='Аватар',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])
    bio = models.TextField(max_length=500, blank=True, verbose_name='Информация о себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    class Meta:
        ordering = ('user', )
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'slug': self.slug})

    def is_online(self):
        last_seen = cache.get(f'last-seen-{self.user.id}')

        if last_seen and timezone.now() < last_seen + timezone.timedelta(seconds=120):
            return True
        return False
