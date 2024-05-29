from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from rest_framework.response import Response
from .models import Flight,Reservation
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FlightSerializer,ReservationSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
import stripe
from django.conf import settings


class LoginView(TokenObtainPairView):
    '''
        Kullanici girisi icin jwt token'lari olusturan gorunum!
    '''
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
    def post(self,request,*args, **kwargs):
        '''
            Kullanici adi sifre ile token'lari olusturuyor
        '''
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            #Basarili giris durumunda token'lari dondur
            return super().post(request, *args, **kwargs)
        else:
            #Gecersiz giris durumunda hata mesaji dondur
            return Response(serializer.errors, status=400)


#Method1

# class FlightCreateAPIView(APIView):
#     def post(self,request):
#         serializer = FlightSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Method2
class FlightCreateAPIView(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# Method 1
class FlightDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    #veritabanindan ucus nesnesini getirir
    def get_object(self,pk):
        try:
            return Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self,request, pk,format=None):
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
    
    def put(self,request, pk, format=None):
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_Valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def patch(self,request,pk,format=None):
    #     flight = self.get_object(pk)
    #     serializer = FlightSerializer(flight, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self,request, pk, format=None):
        flight = self.get_object(pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     


# Method2
# class FlightRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer        
    
  
class FlightListView(APIView):
    def get(self,request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class FlightSearchView(APIView):
    def get(self,request):
        departure_city = request.query_params.get('departure_city',None)
        arrive_city = request.query_params.get('arrive_city', None)
        departure_date = request.query_params.get('departure_date', None)
        
        flights = Flight.objects.all()
        
        if departure_city:
            flights = flights.filter(departure_city__icontains=departure_city)
        if arrive_city:
            flights = flights.filter(arrive_city__icontains = arrive_city)
        if departure_date:
            flights = flights.filter(departure_date__icontains = departure_date)
        
        
        serializer = FlightSerializer(flights, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
             
    
# class FlightSearchView(APIView):
#     def post(self,request):
#         departure_sity = request.data.get('departure_sity')
#         arrive_city = request.data.get('arrivel_city')
#         departure_date = request.data.get('departure_date')
        
        
#         # Flight modelindeki kayıtları filtreler:
#         flights = Flight.objects.filter(
#             departure_city__icontains = departure_sity,
#             arrivel_city__icontains = arrive_city,
#             departure_date = departure_date
#         )    
        
#         serializer = FlightSerializer(flights, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
        
# -----> FlightFare yeniden yazilmali!        

# class FlightFareAPIView(APIView):
#     def get(self,request,flight_id):
#         try:
#             flight_fare = FlightFare.objects.get(flight_id=flight_id)
#             data = {
#                 # 'flight_id': flight_fare.flight_id,
#                 # 'departure_id': flight_fare.departure_date,
#                 # 'departure_time': flight_fare.departure_time,
#                 # 'arrivel_date': flight_fare.arrival_date,
#                 # 'arrival_time': flight_fare.arrival_time,
#                 # 'origin_airport': flight_fare.origin_airport,
#                 # 'destination_airport': flight_fare.destination_airport,
#                 # 'airline': flight_fare.airline,
#                 'seat_class': flight_fare.seat_class,
#                 'base_fare': flight_fare.base_fare,
#                 'taxes_and_fees': flight_fare.taxes_and_fees,
#                 'total_fare': flight_fare.total_fare
#             }
#             return Response(data, status=status.HTTP_200_OK)
#         except Flight.DoesNotExist:
#             return Response({'error': 'Flight not found '}, status=status.HTTP_404_NOT_FOUND)
        


class ReservationListAPIView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            reservations = Reservation.objects.filter(user=request.user)
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ReservationDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        reservation = self.get_object(pk)
        if not reservation:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    
    def put(self,request,pk):
        reservation = self.get_object(pk)
        if not reservation:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    def delete(self,request,pk):
        reservation = self.get_object(pk)
        if not reservation:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
            
