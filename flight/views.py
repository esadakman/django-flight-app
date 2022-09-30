from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from rest_framework import viewsets
from .models import Flight, Passenger, Reservation
from .permissions import IsStafforReadOnly
from datetime import datetime, date

# GET, POST, PUT, DELETE, PATCH
# ! reservationView'da yaptığımız stuuf'sa tüm veriler değilse sadece ilgili verileri gösterme işlemini burada da gerçekleştiroruz ⬇️


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # * oluşturduğumuz permission'ı view'ımıza ekliyoruz
    permission_classes = (IsStafforReadOnly,)

# ! staff userların flightları görüntülerken aynı zamanda  yapılan rezarvasyonları da görmesi için queryset'te yaptığımız gibi serializer_class'ımızıda override etmemiz gerekiyor
    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            # ? user stuff'sa bütün veriler
            return StaffFlightSerializer
            # ? değilse sadece ilgili kullanıcının verileri
        return serializer
# ! kullanıcıların ilgili tarihten önce ki uçuşları görmemeleri için ⬇️
    def get_queryset(self):
        # ? mevcut zamanı alıyoruz
        now = datetime.now()
        # ? saatin formatını current_time ile değiştiriyoruz
        current_time = now.strftime('%H:%M:%S') 
        today = date.today()

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            # ! öncelikle bugünden sonraki uçuşları çağırdık ⬇️
            queryset = Flight.objects.filter(date_of_departure__gt=today)
            if Flight.objects.filter(date_of_departure=today):
            # ! daha sonra ise bugün olup mevcut saatten sonra olan uçuşları listeliyoruz
                today_qs = Flight.objects.filter(
                    date_of_departure=today).filter(etd__gt=current_time)
                # ! son olarak ise elimizde ki queryset'leri birleştiriyoruz
                queryset = queryset.union(today_qs)
            return queryset


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 

# ! request.user stuff'sa queryset'te yazan bütün verileri çekmek için ve stuff olamdığı durumda da sadece ilgili user'a ait bilgileri getirmek için default olarak gelen queryset'i değiştirmemiz için queryset'i override yapıyoruz ⬇️ 

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            # ? user stuff'sa bütün veriler
            return queryset
            # ? değilse sadece ilgili kullanıcının verileri
        return queryset.filter(user=self.request.user)
