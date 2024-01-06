from django.db import models

class Someinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    information = models.TextField()
    email_address = models.EmailField()

    def __str__(self) -> str:
        return self.information

