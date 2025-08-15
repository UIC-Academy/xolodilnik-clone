from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sponsor(BaseModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="sponsors")

    def __str__(self):
        return self.name
