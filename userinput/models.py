from django.db import models

class user_validation(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    case_number = models.CharField(max_length=100)
    prediction_1 = models.CharField(max_length=100)
    prediction_2 = models.CharField(max_length=100)
    prediction_3 = models.CharField(max_length=100)
    recommendation_1 = models.CharField(max_length=100)
    recommendation_2 = models.CharField(max_length=100)
    recommendation_3 = models.CharField(max_length=100)
# Create your models here.
