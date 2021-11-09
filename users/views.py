from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from users.serializers import UserSerializer
from .models import User

class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)
 
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
 
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                token = user.token
                user_details = {}
                user_details['username'] = user.username
                user_details['first_name'] = user.first_name
                user_details['last_name'] = user.last_name
                user_details['token'] = token

                return Response(user_details, status=status.HTTP_200_OK)
 
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)

# class RegistrationAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         user = request.data

#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.get(email=email, password=password)

#         if user:
#             try:
#                 # payload = jwt_payload_handler(user)
#                 token = user.token
#                 user_details = {}
#                 user_details['first_name'] = user.first_name
#                 user_details['token'] = token
#                 return Response(user_details, status=status.HTTP_200_OK)

#             except Exception as e:
#                 raise e

#         else:
#             return Response('Неверные данные', status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         return Response('Введите данные')


# class UserProfileView(APIView):
#     permission_classes=[IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         user = request.data

#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
