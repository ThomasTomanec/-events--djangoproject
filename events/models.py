from django.db import models

class MemberClient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    photo = models.ImageField(upload_to='client_photos/', blank=True, null=True)  # Přidáno pole pro fotku

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SportEvent(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    result = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey(MemberClient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
