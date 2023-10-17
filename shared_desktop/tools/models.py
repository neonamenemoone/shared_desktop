"""tools models configuration."""
from django.db import models


class Central(models.Model):
    """Модель координации."""
    ip_address = models.GenericIPAddressField(
        verbose_name='IP Address',
        protocol='both',
        unique=True
    )
    phase_value = models.PositiveSmallIntegerField(
        verbose_name='phase_value',
        choices=[
            (0, 'LOCAL'),
            (2, '1 фаза'),
            (3, '2 фаза'),
            (4, '3 фаза'),
            (5, '4 фаза'),
            (6, '5 фаза'),
            (7, '6 фаза'),
            (8, '7 фаза'),
            (1, '0 фаза'),
        ]
    )

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = 'Техническая координация.'
        verbose_name_plural = 'Техническая координация'
