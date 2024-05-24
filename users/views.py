from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from rest_framework.response import Response
from .models import Flight
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FlightSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import generics

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
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# Method 1
class FlightDetailAPIView(APIView):
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
    
    def patch(self,request,pk,format=None):
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self,request, pk, format=None):
        flight = self.get_object(pk)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     


# Method2
# class FlightRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Flight.objects.all()
#     serializer_class = FlightSerializer        
    
  
class FlighListView(APIView):
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
        

        