from django.http.response import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from admin_side.models import Tenants
from admin_side.serializers import TenantsrSerializer



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
        try:
            tenant.delete() 
        except Exception as e:
            # pass
            print(e)
        return JsonResponse({'message': 'Tenant was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


