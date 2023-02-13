from django.db import models

# Create your models here.
class RegistroCrons(models.Model):
    titulo = models.CharField(max_length=250, blank=False, null=False)
    sucesso = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Registro CRON'
        verbose_name_plural = 'Registros CRON'


    def __str__(self):
        return '{} - {}'.format(self.titulo, self.data)