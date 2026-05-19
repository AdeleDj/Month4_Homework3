from django.views import generic
from .models import TourCompany, Service
from django.db.models import Avg, Q


class ServiceListView(generic.ListView):
    template_name = 'horse_tour/service_list.html'
    context_object_name = 'page_obj'
    model = Service
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        services = self.model.objects.all()
        if query:
            services = services.filter(
                Q(name__icontains=query)
            )
        return services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    # def service_list(request):
    #     query = request.GET.get('q')
    #     services = Service.objects.all()
    #     if query:
    #         services = services.filter(Q(name__icontains=query))
    #     paginator = Paginator(services, 3)
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'horse_tour/service_list.html', {'page_obj': page_obj, 'query': query})


class IndexView(generic.ListView):
    template_name = 'horse_tour/index.html'
    context_object_name = 'companies'
    model = TourCompany

    def get_queryset(self):
        return self.model.objects.all().annotate(
            avg_rating=Avg('review__rating')
        )

    # def index(request):
    #     companies = TourCompany.objects.all().annotate(avg_rating=Avg('review__rating'))
    #     return render(request, 'horse_tour/index.html', {'companies': companies})