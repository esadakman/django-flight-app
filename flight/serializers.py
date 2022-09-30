from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "flight_number",
            "operating_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Reservation
    #     fields = "__all__"
 # ! bu şekilde ⬆️ yazdığımız zaman dönen data kullanışlı olmadığı için yeni bir passenger serializer ve ReservationSerializer'ı baştan yazıyoruz
    # ? Birden fazla objeye passenger'ı göndereceğim için many=True yazıyorum
    passenger = PassengerSerializer(many=True, required=True)
    flight = serializers.StringRelatedField()  # default read_only=True
    # ! sadece StringRelatedField yazdığım zaman string yazarak object create edemiyorum, bu yüzden ⬇️
    flight_id = serializers.IntegerField(write_only=True) # ? flight id'yi write_only yapmış oluyoruz
    # ! user içinde flight'da yaptıklarımızın aynısını yapıyoruz ⬇️
    user = serializers.StringRelatedField()    # default read_only=True
    user_id = serializers.IntegerField(write_only=True, required=False) # ? user bilgisini isteği atan user bilgisinden aldığımız için bu kısma required=False yazıyoruz

    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",  # GET
            "flight_id",  # POST
            "user",  # GET
            "user_id",  # POST
            "passenger"
        )

# ! reservation serializer'de oluşturulan reservationları burda create edemediğimiz için models.Reservation'da create etmem gerekiyor
# ! passengerlar'ı ise ayrı bir şekilde çekip Passenger tabloma create etmem gerekiyor
# ! gelen bu data'ları yakalıyacağım yer ise ModelSerializer'da da yer alan create metodudur.
# ! bu create metodunu alıp 
    def create(self, validated_data):
        # ? gelen datamı passenger_data'ya pop() ile atıyorum
        passenger_data = validated_data.pop('passenger')
        # ? rezervasyonu create eden user'ı otomatik almak için ise validated_data'ya aktif user_id'yi ekliyorum
        validated_data['user_id'] = self.context['request'].user.id
        # ? artık validated_data'mla rezervation create edebilirim
        reservation = Reservation.objects.create(**validated_data)
        # ? birden fazla datayı yazmak için passenger data'mı for loop'a içine yazıp create ediyorum
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
        # ? son olarak ise bu oluşturduğumuz passengerları reservation objemin passenger'ına bağlamamız lazım
            reservation.passenger.add(pas)
        reservation.save()
        return reservation


# ! yukarda ki flight serializerımızdan farklı olarak reservation serializers'ımızıda koyduğumuz yeni bir StaffFlightSerializer yazıyoruz
class StaffFlightSerializer(serializers.ModelSerializer):
    # ? models'da vermiş oldumuz related name'i kullanarak ReservationSerializer'ı çağırıyoruz    
    reservation = ReservationSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = "__all__"