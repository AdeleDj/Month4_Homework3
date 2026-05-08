from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm


#read list
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/list.html', {'bookings': bookings})


#create
def booking_create(request):
    form = BookingForm(request.POST)

    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('/booking_list/')

    return render(request, 'bookings/form.html', {'form': form})


#update
def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id)
    form = BookingForm(request.POST, instance=booking)

    if form.is_valid():
        form.save()
        return redirect('/booking_list/')

    return render(request, 'bookings/form.html', {'form': form})


#delete
def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.delete()
        return redirect('/booking_list/')

    return render(request, 'bookings/delete.html', {'booking': booking})


def booking_detail(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'bookings/detail.html', {'booking': booking})
