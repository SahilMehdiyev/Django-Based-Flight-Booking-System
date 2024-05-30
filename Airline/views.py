from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import AirlineSerializer
from .models import Airline


class AirlineListView(APIView):
    def get(self,request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        
            