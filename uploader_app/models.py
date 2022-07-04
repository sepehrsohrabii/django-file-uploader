from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField()

    @property
    def file_name(self):
        fileName = self.file.name
        return fileName

    @property
    def file_size(self):
        fileSize = self.file.size
        return fileSize

    @property
    def file_type(self):
        import os
        fileType = os.path.splitext(self.file.name)[1]
        return fileType


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

