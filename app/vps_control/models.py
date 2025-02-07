import uuid

from django.db import models

VPS_SERVER_STATUSES = [
    ("started", "Started"),
    ("blocked", "Blocked"),
    ("stopped", "Stopped"),
]


# Create your models here.
class VPS(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(choices=VPS_SERVER_STATUSES, default="stopped")

    def __str__(self):
        return f"VPS № {self.uid} - {self.status}"
