from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from django.db.models import Q
from django.views import generic


class BookingListView(generic.ListView):
    template_name = 'bookings/list.html'
    context_object_name = 'page_obj'
    model = Booking
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        bookings = self.model.objects.all()
        if query:
            bookings = bookings.filter(
                Q(company__name__icontains=query) |
                Q(user__username__icontains=query)
            )
        return bookings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    # def booking_list(request):
    #     query = request.GET.get('q')
    #     bookings = Booking.objects.all()
    #     if query:
    #         bookings = bookings.filter(...)
    #     paginator = Paginator(bookings, 3)
    #     page_obj = paginator.get_page(page_number)
    #     return render(request, 'bookings/list.html', {'page_obj': page_obj, 'query': query})


class BookingCreateView(generic.CreateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return super().form_valid(form)

    # def booking_create(request):
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         booking = form.save(commit=False)
    #         booking.user = request.user
    #         booking.save()
    #         return redirect('/booking_list/')
    #     return render(request, 'bookings/form.html', {'form': form})


class BookingUpdateView(generic.UpdateView):
    template_name = 'bookings/form.html'
    form_class = BookingForm
    model = Booking
    success_url = reverse_lazy('booking_list')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, id=self.kwargs.get('id'))

    # def booking_update(request, id):
    #     booking = get_object_or_404(Booking, id=id)
    #     form = BookingForm(request.POST, instance=booking)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/booking_list/')
    #     return render(request, 'bookings/form.html', {'form': form})


class BookingDeleteView(generic.DeleteView):
    template_name = 'bookings/delete.html'
    model = Booking
    context_object_name = 'booking'
    success_url = reverse_lazy('booking_list')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, id=self.kwargs.get('id'))

    # def booking_delete(request, id):
    #     booking = get_object_or_404(Booking, id=id)
    #     if request.method == 'POST':
    #         booking.delete()
    #         return redirect('/booking_list/')
    #     return render(request, 'bookings/delete.html', {'booking': booking})


class BookingDetailView(generic.DetailView):
    template_name = 'bookings/detail.html'
    context_object_name = 'booking'
    model = Booking

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, id=self.kwargs.get('id'))

    # def booking_detail(request, id):
    #     booking = get_object_or_404(Booking, id=id)
    #     return render(request, 'bookings/detail.html', {'booking': booking})