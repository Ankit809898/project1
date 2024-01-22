from rest_framework import serializers
from .models import Bank, Card, RewardsProgram, SpendingCategory, FeesAndCharges, AdditionalInformation, Customer

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class RewardsProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardsProgram
        fields = '__all__'

class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingCategory
        fields = '__all__'

class FeesAndChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesAndCharges
        fields = '__all__'

class AdditionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    rewards_program = RewardsProgramSerializer(many=True, read_only=True)
    spending_categories = SpendingCategorySerializer(many=True, read_only=True)
    fees_and_charges = FeesAndChargesSerializer(read_only=True)
    additional_information = AdditionalInformationSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
