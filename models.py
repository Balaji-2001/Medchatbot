from django.db import models

class MedicalInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=5)
    weight = models.FloatField()
    additional_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"
