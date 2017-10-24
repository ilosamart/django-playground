from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=50, blank=False)
    
    class Meta:
        db_table = 'tasks'
    
