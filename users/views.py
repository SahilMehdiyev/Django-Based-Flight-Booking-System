from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer
from rest_framework.response import Response


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


  