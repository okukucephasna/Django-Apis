from django.db import models

class MyModel(models.Model):
    # Define your fields here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as needed

    def __str__(self):
        return self.field1  # Modify the display value as needed
