from django.db import models
from django.contrib.auth.models import User
from horse_tour.models import TourCompany

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    people_count = models.IntegerField()

    def __str__(self):
        return f'{self.user}---{self.company} ({self.date})'
    
    