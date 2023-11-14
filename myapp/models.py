from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    id = models.IntegerField(primary_key=True, blank=True)
    sana = models.DateField(blank=True)



    def __str__(self) -> str:
        return f"{self.title}, {self.id}, {self.sana}"