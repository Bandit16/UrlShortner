from django.db import models
from django.contrib.auth.models import User

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField(null=True, blank=True , default=None)

    def __str__(self):
        return self.short_code

class ClickLog(models.Model):
    url = models.ForeignKey(
        ShortURL,
        on_delete=models.CASCADE
    )

    ip_address = models.GenericIPAddressField()

    clicked_at = models.DateTimeField(
        auto_now_add=True
    )