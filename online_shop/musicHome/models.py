from django.db import models

class Users(models.Model):
    email = models.EmailField()
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    is_admin = models.BooleanField()

    class Meta:
        verbose_name = 'Пользователи сайта'
        verbose_name_plural = 'Пользователи сайта'
        #ordering = []

#def get_absolute_url(self):
 #   return reverse('post', kwards={})
