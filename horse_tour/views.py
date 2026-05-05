from django.shortcuts import render
from .models import TourCompany
from django.db.models import Avg


def index(request):
    companies = TourCompany.objects.all().annotate(
        avg_rating=Avg('review__rating')
    )

    return render(request, 'horse_tour/index.html', {
        'companies': companies
    })