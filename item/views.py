from django.shortcuts import get_object_or_404, render ,redirect
from .models import Cars, Reservation,types
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect ,HttpResponseForbidden
from django.contrib.auth.models import User


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Cars, pk=pk)

    return render(request, 'cars/detail.html', {
        'cars': item
    })

@login_required
def reserve_car(request, pk):
    car = get_object_or_404(Cars, pk= pk)
    if request.method == 'POST':  
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.car = car
            car.is_reserved = True
            car.save()
            reservation.save()
            return HttpResponseRedirect('/items/res')
             
    else:
        
        form = ReservationForm()
        form.fields['car'].queryset = Cars.objects.filter(pk=pk)
    return render(request, 'cars/reserve_car.html', {
        'cars': car , 'form': form 
        })




@receiver(post_delete, sender=Reservation)
def no_reservation(sender, instance, **kwargs):
    car = instance.car
    car.is_reserved = False
    car.save()

def items(request):
    query = request.GET.get('query', '')
    car = Cars.objects.filter(is_reserved=False)
    categories= types.objects.all()
    types_id=request.GET.get('types', 0)
    if query:
        car = car.filter(Q(make__icontains=query)|Q(model__icontains=query))
    if types_id :
        car = car.filter(categories=types_id)

    return render(request , 'cars/items.html',{
        'cars': car ,
        'query' : query,
        'types' : categories,
        'types_id': int(types_id)
        
    })

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'cars/user_reservation.html', {
        'reservations': reservations,
        
        })


@login_required
def user_canc_reservation(request, pk):
    reservation = get_object_or_404(Reservation , pk=pk , user = request.user)
    if request.method == 'POST':
        reservation.car.is_reserved = False
        reservation.car.save()
        reservation.delete()
        messages.success(request , "Your reservation has been deleted ")
        return HttpResponseRedirect('/items/res')
        
    else :
        return render(request, 'cars/reservation_cancel.html', {
            'reservation': reservation,
        })
    

@login_required
def admin_dash(request):
    if request.user.is_staff:
        reservation = Reservation.objects.all()
        users= User.objects.all()
        return render(request, 'cars/admin_dash.html', {'reservations': reservation, 'users': users})
    else:
            return HttpResponseForbidden()

@login_required
def admin_dele_res(request , pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.car.is_reserved = False
        reservation.car.save()
        reservation.delete()
        return HttpResponseRedirect('/items/dash')

