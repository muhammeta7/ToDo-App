from django.db import models
from datetime import datetime
# from __future__ import unicode_literals

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank = True)

