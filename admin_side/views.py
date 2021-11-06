from django.contrib.auth.models import User
from django.http.response import JsonResponse
# from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions

from admin_side.models import Tenants
from client_side.models import Premises
from admin_side.serializers import TenantsrSerializer, UserSerializer
from client_side.serializers import PremisesSerializer


@api_view(['GET', 'POST'])
def tenant_list(request):
    tenants = Tenants.objects.all()

    if request.method == 'GET': 
        tenant_name = request.GET.get('tenant_name', None)
        if tenant_name is not None:
            tenants = tenants.filter(tenant_name__icontains=tenant_name)

        tenants_serializer = TenantsrSerializer(tenants, many=True)
        return JsonResponse(tenants_serializer.data, safe=False)

    elif request.method == 'POST':
        tenant_data = JSONParser().parse(request)
        tenants_serializer = TenantsrSerializer(data=tenant_data)
        if tenants_serializer.is_valid():
            tenants_serializer.save()
            return JsonResponse(tenants_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tenants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])  
def tenant_detail(request, pk):
    tenant = Tenants.objects.get(pk=pk)

    if request.method == 'GET': 
        tenants_serializer = TenantsrSerializer(tenant) 
        return JsonResponse(tenants_serializer.data)

    elif request.method == 'PUT': 
        tenant_data = JSONParser().parse(request) 
        tenants_serializer = TenantsrSerializer(tenant, data=tenant_data) 
        if tenants_serializer.is_valid(): 
            tenants_serializer.save() 
            return JsonResponse(tenants_serializer.data) 
        return JsonResponse(tenants_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        tenant.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def premise_bytype_list(request):
    premises = Premises.objects.all()

    if request.method == 'GET': 
        premise_type = request.GET.get('premise_type', None)
        coworkings = premises.filter(premise_type__exact=premise_type)

        premise_serializer = PremisesSerializer(coworkings, many=True)
        return JsonResponse(premise_serializer.data, safe=False)

class ProfileView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [TokenAuthentication]

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email': user.email
        })


