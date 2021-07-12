# # from django.shortcuts import render
# # from django.http import HttpResponse

# # Create your views here.
# # def index(request):
# #     return HttpResponse("Это страница заглушка.")

# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from .models import Tenants, Individuals, Entits, Individual_entrepreneurs, Discount_cards, Deals
# from .serializers import TenantsrSerializer, IndividualsSerializer, EntitsSerializer, IndividualEntrepreneursSerializer, DiscountCardsSerializer, DealsSerializer

# from django.core.files.storage import default_storage

# # Create your views here.
# @csrf_exempt
# def tenantApi(request,id=0):
#     if request.method=='GET':
#         tenants = Tenants.objects.all()
#         tenants_serializer = TenantsrSerializer(tenants, many=True)
#         return JsonResponse(tenants_serializer.data, safe=False)

#     elif request.method=='POST':
#         tenant_data=JSONParser().parse(request)
#         tenant_serializer = TenantsrSerializer(data=tenant_data)
#         if tenant_serializer.is_valid():
#             tenant_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         tenant_data = JSONParser().parse(request)
#         tenant=Tenants.objects.get(id=tenant_data['id'])
#         tenant_serializer=TenantsrSerializer(tenant,data=tenant_data)
#         if tenant_serializer.is_valid():
#             tenant_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         tenant=Tenants.objects.get(id=id)
#         tenant.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# @csrf_exempt
# def individualApi(request,id=0):
#     if request.method=='GET':
#         individuals = Individuals.objects.all()
#         individuals_serializer = IndividualsSerializer(individuals, many=True)
#         return JsonResponse(individuals_serializer.data, safe=False)

#     elif request.method=='POST':
#         individual_data=JSONParser().parse(request)
#         individual_serializer = IndividualsSerializer(data=individual_data)
#         if individual_serializer.is_valid():
#             individual_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         individual_data = JSONParser().parse(request)
#         individual=Individuals.objects.get(id=individual_data['id'])
#         individual_serializer=IndividualsSerializer(individual,data=individual_data)
#         if individual_serializer.is_valid():
#             individual_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         individual=Individuals.objects.get(id=id)
#         individual.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# @csrf_exempt
# def entitstApi(request,id=0):
#     if request.method=='GET':
#         entits = Entits.objects.all()
#         entits_serializer = EntitsSerializer(entits, many=True)
#         return JsonResponse(entits_serializer.data, safe=False)

#     elif request.method=='POST':
#         entit_data=JSONParser().parse(request)
#         entit_serializer = EntitsSerializer(data=entit_data)
#         if entit_serializer.is_valid():
#             entit_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         entit_data = JSONParser().parse(request)
#         entit=Entits.objects.get(id=entit_data['id'])
#         entit_serializer=EntitsSerializer(entit,data=entit_data)
#         if entit_serializer.is_valid():
#             entit_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         entit=Entits.objects.get(id=id)
#         entit.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# @csrf_exempt
# def individualEntrepreneursApi(request,id=0):
#     if request.method=='GET':
#         indEntreps = Individual_entrepreneurs.objects.all()
#         indEntreps_serializer = IndividualEntrepreneursSerializer(indEntreps, many=True)
#         return JsonResponse(indEntreps_serializer.data, safe=False)

#     elif request.method=='POST':
#         indEntreps_data=JSONParser().parse(request)
#         indEntreps_serializer = IndividualEntrepreneursSerializer(data=indEntreps_data)
#         if indEntreps_serializer.is_valid():
#             indEntreps_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         indEntreps_data = JSONParser().parse(request)
#         indEntrep=Individual_entrepreneurs.objects.get(id=indEntreps_data['id'])
#         indEntrep_serializer=IndividualEntrepreneursSerializer(indEntrep,data=indEntreps_data)
#         if indEntrep_serializer.is_valid():
#             indEntrep_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         indEntrep=Individual_entrepreneurs.objects.get(id=id)
#         indEntrep.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# @csrf_exempt
# def discountApi(request,id=0):
#     if request.method=='GET':
#         discountCards = Discount_cards.objects.all()
#         discountCards_serializer = DiscountCardsSerializer(discountCards, many=True)
#         return JsonResponse(discountCards_serializer.data, safe=False)

#     elif request.method=='POST':
#         discountCard_data=JSONParser().parse(request)
#         discountCard_serializer = DiscountCardsSerializer(data=discountCard_data)
#         if discountCard_serializer.is_valid():
#             discountCard_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         discountCard_data = JSONParser().parse(request)
#         discountCard=Discount_cards.objects.get(id=discountCard_data['id'])
#         discountCard_serializer=DiscountCardsSerializer(discountCard,data=departmdiscountCard_dataent_data)
#         if discountCard_serializer.is_valid():
#             discountCard_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         discountCard=Discount_cards.objects.get(id=id)
#         discountCard.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# @csrf_exempt
# def dealsApi(request,id=0):
#     if request.method=='GET':
#         deals = Deals.objects.all()
#         deals_serializer = DealsSerializer(deals, many=True)
#         return JsonResponse(deals_serializer.data, safe=False)

#     elif request.method=='POST':
#         deal_data=JSONParser().parse(request)
#         deal_serializer = DealsSerializer(data=deal_data)
#         if deal_serializer.is_valid():
#             deal_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         deal_data = JSONParser().parse(request)
#         deal=Deals.objects.get(id=deal_data['id'])
#         deal_serializer=DealsSerializer(deal,data=deal_data)
#         if deal_serializer.is_valid():
#             deal_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         deal=Deals.objects.get(id=id)
#         deal.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)