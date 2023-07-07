from django.db import models


class line_user(models.Model):
    userId = models.CharField(max_length=33)

class line_group(models.Model):
    groupId = models.CharField(max_length=33)
    userId = models.ForeignKey(line_user, on_delete=models.CASCADE)
# Create your models here.
