from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=124)
    record_date = models.DateTimeField()
    priority = models.BooleanField(default=False)

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()

    