from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics

from django.core.mail import send_mail
from django.contrib.auth.models import User
from .serializers import SignupSerializer
from django.utils.timezone import now

from codes.models import Code

class Login(ObtainAuthToken) :
    permission_classes = (AllowAny,)

    def post(self, request) :
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)

        verified = Code.objects.filter(
            user_id=user.pk,
            address=request.META.get('REMOTE_ADDR'),
            is_used=True
        ).exists()

        if verified :
            return Response({
                'token': token[0].key,
                'user_id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_admin': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'verified': True
            })

        else :
            current_code = Code.objects.filter(
                user_id=user.pk,
                address = request.META.get('REMOTE_ADDR'),
                expire_date__gte=now()
            ).exists()

            if not current_code :
                newcode = Code(
                    user_id=user.pk,
                    address=request.META.get('REMOTE_ADDR')
                )
                newcode.codegen()
                newcode.save()

                send_code(user.email, newcode.code)

            return Response({
                'user_id': user.pk,
                'token': token[0].key,
                'verified': False
            })

class Signup(generics.CreateAPIView) :
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = Token.objects.get_or_create(user=user)

        newcode = Code(
            user_id=user.pk,
            address=request.META.get('REMOTE_ADDR')
        )
        newcode.codegen()
        newcode.save()

        send_code(user.email, newcode.code)

        return Response({
            'user_id': user.pk,
            'token': token[0].key,
            'verified': False
        })

class Validation(generics.CreateAPIView) :
    def post(self, request) :
        
        code_exists = Code.objects.filter(
            user_id=request.data.get('user_id'),
            code=request.data.get('code'),
            address = request.META.get('REMOTE_ADDR'),
            expire_date__gte=now(),
            is_used=False
        ).exists()

        if code_exists : 
            code = Code.objects.get(
                user_id=request.data.get('user_id'),
                code=request.data.get('code')
            )

            code.is_used = True
            code.save()

            user = User.objects.get(pk=request.data.get('user_id'))

            return Response({
                'user_id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_admin': user.is_superuser,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'verified': True
            })

        else :
            return Response({
                'verified': code_exists
            })

def send_code(mail='', code='') :
    body = f"""
        Here is your code:
        {code}

        *Remember: this code has an expiration date
        """
    
    try :
        send_mail(
            'Cryptotracker validation code',
            body,
            'Cryptotracker <no-reply@cryptotracker.com>',
            [mail],
            fail_silently=False,
        )

    except :
        print('Error attempting to send code-mail')
        pass