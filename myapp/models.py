from django.db import models

class ServiceCard(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='service_cards/', blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title
