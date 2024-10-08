from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url