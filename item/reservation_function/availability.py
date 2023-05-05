import datetime
from item.models import Cars ,Reservation
def check_availability (c, dd,df):
    v =True
    a=False


    res=Reservation.objects.filter(car=c)
    for r in res :
        if r.start_date > df or r.end_date<dd:
            a=True
        else:
            v=False


    return v