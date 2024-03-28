import datetime
from hotel.models  import Room, Booking



def check_availability(room, check_in, check_out):
    avail_list=[] #list of booleans for each and every booking
    booking_list =Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out< check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list) # all returns true if all of the items in the list are true. 