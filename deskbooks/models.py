from django.db import models
from django.utils.translation import ugettext_lazy as _


class BorderPoint(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Пункт пропуску')
        verbose_name_plural = _('Пункти пропуску')
        ordering = ('code',)

    def __str__(self):
        return self.code
