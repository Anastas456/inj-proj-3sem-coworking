from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from client_side.models import Premises, Rates

from client_side.serializers import PremisesSerializer, RatesSerializer, RentFormSerializer 

@api_view(['GET'])
@permission_classes([AllowAny])
def premise_bytype_list(request):
    premises = Premises.objects.all()

    if request.method == 'GET': 
        premise_type = request.GET.get('premise_type', None)
        filtered_premises = premises.filter(premise_type__exact=premise_type)

        premise_serializer = PremisesSerializer(filtered_premises, many=True)
        return JsonResponse(premise_serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def rate_list(request):
    rates = Rates.objects.all()
    if request.method == 'GET': 
        rate_serializer = RatesSerializer(rates, many=True)
        return JsonResponse(rate_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_premise(request):
    premise_data = JSONParser().parse(request)
    premise_serializer = PremisesSerializer(data=premise_data)
    if premise_serializer.is_valid():
        premise_serializer.save()
        return JsonResponse(premise_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(premise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])  
@permission_classes([IsAuthenticated])
def premise_detail(request, pk):
    premise = Premises.objects.get(pk=pk)

    if request.method == 'GET': 
        premise_serializer = PremisesSerializer(premise) 
        return JsonResponse(premise_serializer.data)

    elif request.method == 'PUT': 
        premise_data = JSONParser().parse(request) 
        premise_serializer = PremisesSerializer(premise, data=premise_data) 
        if premise_serializer.is_valid(): 
            premise_serializer.save() 
            return JsonResponse(premise_serializer.data) 
        return JsonResponse(premise_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        premise.delete() 
        return JsonResponse({'message': 'Premise was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def form_rent_form(request):

    form_data = JSONParser().parse(request)
    form_serializer = RentFormSerializer(data=form_data)
    if form_serializer.is_valid():
        form_serializer.save()
        return JsonResponse(form_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
