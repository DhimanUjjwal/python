import uuid
from django.db import models

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=300, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.email



