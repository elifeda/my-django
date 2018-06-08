from django.db import models
from django.utils import timezone

class Kategori(models.Model):
     kategori_adi = models.CharField(max_length=100) 

class Post(models.Model):
    kategori = models.ForeignKey( Kategori, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
