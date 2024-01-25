from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Card, Bank, RewardsProgram, SpendingCategory, FeesAndCharges, AdditionalInformation, Customer
from .serializers import CardSerializer, BankSerializer, RewardsProgramSerializer, SpendingCategorySerializer, FeesAndChargesSerializer, AdditionalInformationSerializer, CustomerSerializer
# Create your views here.
# credit_cards/views.py


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class RewardsProgramViewSet(viewsets.ModelViewSet):
    queryset = RewardsProgram.objects.all()
    serializer_class = RewardsProgramSerializer


class SpendingCategoryViewSet(viewsets.ModelViewSet):
    queryset = SpendingCategory.objects.all()
    serializer_class = SpendingCategorySerializer

class FeesAndChargesViewSet(viewsets.ModelViewSet):
    queryset = FeesAndCharges.objects.all()
    serializer_class = FeesAndChargesSerializer

class AdditionalInformationViewSet(viewsets.ModelViewSet):
    queryset = AdditionalInformation.objects.all()
    serializer_class = AdditionalInformationSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer