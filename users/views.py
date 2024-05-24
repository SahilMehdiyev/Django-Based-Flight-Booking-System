from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from rest_framework.response import Response
from .models import Flight
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FlightSerializer


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


class FlighListView(APIView):
    def get(self,request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FlightSearchView(APIView):
    def post(self,request):
        departure_sity = request.data.get('departure_sity')
        arrive_city = request.data.get('arrivel_city')
        departure_date = request.data.get('departure_date')
        
        
        # Flight modelindeki kayıtları filtreler:
        flights = Flight.objects.filter(
            departure_city__icontains = departure_sity,
            arrivel_city__icontains = arrive_city,
            departure_date = departure_date
        )    
        
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        