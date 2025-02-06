from django.db import models

# Create your models here.
class VPS(models.Model):
    uid = models.UUIDField()
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField()

    def __str__(self):
        return f'{self.cpu} cpu; {self.ram} ram; {self.hdd} hdd; {self.status}'