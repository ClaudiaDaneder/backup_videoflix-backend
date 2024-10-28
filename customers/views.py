
from customers.tasks import send_activation_email
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def create_superuser(request):
    if get_user_model().objects.count() == 0:
        get_user_model().objects.create_superuser(
            'admin', 
            'deine@email.com',
            'dein-sicheres-passwort'
        )
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists!")


class LoginView(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        customer = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=customer)
        return Response({
            'token': token.key,
            'customer_id': customer.pk,
            'email': customer.email
        })

class RegisterView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()

            customers_group, created = Group.objects.get_or_create(name='Customers')
            customer.groups.add(customers_group)

            customer.is_active = False
            customer.save()

            customer.generate_activation_token()
            send_activation_email(customer)

            return Response({
                'id': customer.id,
                'username': customer.username,
                'email': customer.email,
                'activation_token': customer.activation_token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ActivateAccountView(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data.get('activation_token')

        if not token:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Customer.objects.get(activation_token=token)
        except ObjectDoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = True
        user.save()

        return Response({'success': 'Account activated successfully'}, status=status.HTTP_200_OK)


class UsernameCheck(APIView):
    def get(self, request):
        username = request.GET.get('username', None)
        data = {
            'is_taken': Customer.objects.filter(username__iexact=username).exists()
        }
        return Response(data)


class EmailCheck(APIView):
    def get(self, request):
        email = request.GET.get('email', None)
        data = {
            'is_taken': Customer.objects.filter(email__iexact=email).exists()
        }
        return Response(data)

