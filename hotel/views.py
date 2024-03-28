from django.shortcuts import render ,HttpResponse

from django.views.generic import ListView, FormView , View
from django.urls import reverse

from .models import Room,Booking
from .forms import AvailabilityForm

from hotel.booking_functions.availability import check_availability

# Create your views here.

def RoomListView(request) : 
    room=Room.objects.all()[0]
    room_categories= dict(room.Room_Categories)
    
    room_values=room_categories.values()
    room_list=[]
    for room_category in room_categories:
        room=room_categories.get(room_category)
        room_url=reverse('hotel:RoomDetailView' , kwargs={'category':room_category})
        
        # print(room,room_url)
        room_list.append((room,room_url))
        
        
        
    
    context={
        "room_list":room_list,
    }
    print(room_list)
    return render(request, 'room_list_view.html',context)



class BookingList(ListView) :
    model=Booking

class RoomDetailView(View):
    def get(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        form=AvailabilityForm()
        
        room_list=Room.objects.filter(category=category) 
        
        if len(room_list)>0:
            room=room_list[0]
            room_category= dict(room.Room_Categories).get(room.category,None)
            context={
            'room_category': room_category,
            'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        
        else:
            return HttpResponse('Category Does Not Exist')
        
    
    def post(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        room_list=Room.objects.filter(category=category) 
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        
        
        if len(available_rooms)>0:
         room=available_rooms[0]
         booking=Booking.objects.create(
            user=self.request.user,
            room =room,
            check_in=data['check_in'],
            check_out=data['check_out']

         )

         booking.save() 
         return HttpResponse(booking)
        else :
            return HttpResponse('All of This category of rooms are booked !! Try Another One..Good Luck !!')       
    

class BookingView(FormView):
    form_class= AvailabilityForm
    template_name='availability_form.html'

    def form_valid(self,form):
        data=form.cleaned_data
        room_list=Room.objects.filter(category=data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room,data['check_in'], data['check_out']):
                available_rooms.append(room)
        
        
        if len(available_rooms)>0:
         room=available_rooms[0]
         booking=Booking.objects.create(
            user=self.request.user,
            room =room,
            check_in=data['check_in'],
            check_out=data['check_out']

         )

         booking.save() 
         return HttpResponse(booking)
        else :
            return HttpResponse('All of This category of rooms are booked !! Try Another One..Good Luck !!')